#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""XYZ Stage Controller (PDVCN brand) using Serial and GRBL protocol"""

import logging
import time
from pathlib import Path

import serial

from linum_microscopes.config import config

logging.basicConfig(
    format=f"%(levelname)s - %(asctime)s [{Path(__file__).name}:%(lineno)s | %(funcName)s()] %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S")

# TODOS
# TODO: instead of keeping an internal origin coordinate, use the active coordinate frame.
# TODO: add unittest and integration tests for the stage.

# References
# https://github.com/gnea/grbl/blob/master/doc/markdown
# https://www.sainsmart.com/blogs/news/grbl-v1-1-quick-reference
# https://cncphilosophy.com/grbl-g-code-commands-list/
# documentation G CODE - https://marlinfw.org/meta/gcode/


GRBL_ERROR_CODES = {
    1: "GCode Command letter was not found.",
    2: "GCode Command value invalid or missing.",
    3: "Grbl '$' not recognized or supported.",
    4: "Negative value for an expected positive value.",
    5: "Homing fail. Homing not enabled in settings.",
    6: "Min step pulse must be greater than 3usec.",
    7: "EEPROM read failed. Default values used.",
    8: "Grbl '$' command Only valid when Idle.",
    9: "GCode commands invalid in alarm or jog state.",
    10: "Soft limits require homing to be enabled.",
    11: "Max characters per line exceeded. Ignored.",
    12: "Grbl '$' setting exceeds the maximum step rate.",
    13: "Safety door opened and door state initiated.",
    14: "Build info or start-up line > EEPROM line length",
    15: "Jog target exceeds machine travel, ignored.",
    16: "Jog Cmd missing '=' or has prohibited GCode.",
    17: "Laser mode requires PWM output.",
    20: "Unsupported or invalid GCode command.",
    21: "> 1 GCode command in a modal group in block.",
    22: "Feed rate has not yet been set or is undefined.",
    23: "GCode command requires an integer value.",
    24: "> 1 GCode command using axis words found.",
    25: "Repeated GCode word found in block.",
    26: "No axis words found in command block.",
    27: "Line number value is invalid.",
    28: "GCode Cmd missing a required value word.",
    29: "G59.x WCS are not supported.",
    30: "G53 only valid with G0 and G1 motion modes.",
    31: "Unneeded Axis words found in block.",
    32: "G2/G3 arcs need >= 1 in-plane axis word.",
    33: "Motion command target is invalid.",
    34: "Arc radius value is invalid.",
    35: "G2/G3 arcs need >= 1 in-plane offset word.",
    36: "Unused value words found in block.",
    37: "G43.1 offset not assigned to tool length axis.",
    38: "Tool number greater than max value."
}
GRBL_SETTINGS_DEFINITIONS = {
    "$0": "Step pulse, microseconds",
    "$1": "Step idle delay, milliseconds",
    "$2": "Step port invert, XYZmask*",
    "$3": "Direction port invert, XYZmask*",  # The direction each axis moves.
    "$4": "Step enable invert, (0=Disable, 1=Invert)",
    "$5": "Limit pins invert, (0=N-Open. 1=N-Close)",
    "$6": "Probe pin invert, (0=N-Open. 1=N-Close)",
    "$10": "Status report, '?' status.  0=WCS position, 1=Machine position, 2= plan/buffer and WCS position, 3=plan/buffer and Machine position.",
    "$11": "Junction deviation, mm",
    "$12": "Arc tolerance, mm",
    "$13": "Report in inches, (0=mm. 1=Inches)",  # **: Reporting units are independent of the units set in the Gcode!
    "$20": "Soft limits, (0=Disable. 1=Enable, Homing must be enabled)",
    "$21": "Hard limits, (0=Disable. 1=Enable)",
    "$22": "Homing cycle, (0=Disable. 1=Enable)",
    "$23": "Homing direction invert, XYZmask* Sets which corner it homes to.",
    "$24": "Homing feed, mm/min",
    "$25": "Homing seek, mm/min",
    "$26": "Homing debounce, milliseconds",
    "$27": "Homing pull-off, mm",
    "$30": "Max spindle speed, RPM",
    "$31": "Min spindle speed, RPM",
    "$32": "Laser mode, (0=Off, 1=On)",
    "$100": "Number of X steps to move 1mm",
    "$101": "Number of Y steps to move 1mm",
    "$102": "Number of Z steps to move 1mm",
    "$110": "X Max rate, mm/min",
    "$111": "Y Max rate, mm/min",
    "$112": "Z Max rate, mm/min",
    "$120": "X Acceleration, mm/sec^2",
    "$121": "Y Acceleration, mm/sec^2",
    "$122": "Z Acceleration, mm/sec^2",
    "$130": "X Max travel, mm Only for Homing and Soft Limits.",
    "$131": "Y Max travel, mm Only for Homing and Soft Limits.",
    "$132": "Z Max travel, mm Only for Homing and Soft Limits.",
}


class PDVStageController:
    def __init__(self, port: str):
        """
        Parameters
        ----------
        port
            Serial port to connect to the stage.
        """
        # Connect to the stage xyz and wake it up
        self.serial = serial.Serial(
            port,
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        self.origin_position = [0.0, 0.0, 0.0]

    def __del__(self):
        self.disconnect()

    def send_command(self, command: str):
        """
        Send a grbl command to the stage using serial communication.

        Parameters
        ----------
        command
             gcode command to be sent

        Returns
        -------
        list / str
            Command response
        """
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()

        # Prepare the command
        command_encoded = command
        if not command_encoded.endswith("\r\n"):
            command_encoded += "\r\n"
        command_encoded = str.encode(command_encoded)

        # Send the command and wait for a response
        self.serial.write(command_encoded)
        time.sleep(0.05)  # Wait a few milliseconds for the response to be ready

        # Read the response
        response = []
        new_line = self.serial.readline().strip().decode("utf-8")
        response.append(new_line)
        while response[-1] != "ok":
            # Check if the value is an error
            if response[-1].startswith("error"):
                error_response = response[-1]
                error_code = int(error_response.split(":")[1])
                error_message = f"Command: {command} caused GRBL {error_response} ({GRBL_ERROR_CODES[error_code]})"
                logging.error(error_message)
            new_line = self.serial.readline().strip().decode("utf-8")
            response.append(new_line)
        if "ok" in response: response.remove("ok")  # Remove the last ok value
        if len(response) == 1:
            response = response[0]
        logging.debug([command, response])  # DEBUG
        return response

    def connect(self):
        """
        Connecte les stages XYZ

        Raises:
            ConnectionError: En cas d'erreur de connexion série.
            PermissionError: En cas de refus d'accès au port série.
        """
        time.sleep(2)
        self.serial.reset_input_buffer()
        self.serial.reset_output_buffer()
        self.wake_up()

        # Set the default GRBL settings
        self.send_command("$10=3")  # Set the status report format
        self.send_command("$20=1")  # Activate the soft limits

    def configure(self, settings: dict):
        """
        Configure the stage with the given settings
        Parameters
        ----------
        settings
            Dictionary of settings to configure
        """
        if "x_axis_travel" in settings:
            self.send_command(f"$130={settings['x_axis_travel']}")
        if "x_axis_max_position" in settings:
            self.send_command(f"$130={settings['x_axis_max_position']}")
        if "top_rotation_travel" in settings:
            self.send_command(f"$130={settings['top_rotation_travel']}")
        if "y_axis_travel" in settings:
            self.send_command(f"$131={settings['y_axis_travel']}")
        if "y_axis_max_position" in settings:
            self.send_command(f"$131={settings['y_axis_max_position']}")
        if "bottom_rotation_travel" in settings:
            self.send_command(f"$131={settings['bottom_rotation_travel']}")
        if "z_axis_travel" in settings:
            self.send_command(f"$132={settings['z_axis_travel']}")
        if "homing_direction" in settings:
            self.send_command(f"$23={settings['homing_direction']}")
        if "axis_direction" in settings:
            self.send_command(f"$3={settings['axis_direction']}")
        if "z_step_for_1mm" in settings:
            self.send_command(f"$102={settings['z_step_for_1mm']}")

    def disconnect(self):
        self.serial.close()

    def wake_up(self):
        """
        Waking up the stage to enable serial communication
        """
        # Hit enter a few times to wake the stage.
        self.send_command("\r\n\r\n")
        time.sleep(2.0)

    def homing(self):
        """
        Homing action.
        """
        logging.info("Homing the stage")
        self.send_command("$H")

        # Set the first coordinate system origin (G54)
        pos = self.position  # Machine position
        self.send_command(f"G10L2 X{pos[0]} Y{pos[1]} Z{pos[2]}")

        # Set the origin position
        self.origin_position = self.status_report['pos_mm']

    def abort(self):
        """
        Soft-Reset.
        Notes
        -----
        * Immediately halts and safely resets Grbl without a power-cycle.
        * Accepts and executes this command at any time.
        * If reset while in motion, Grbl will throw an alarm to indicate position may be lost from the motion halt.
        * If reset while in not motion, position is retained and re-homing is not required.
        """
        self.serial.write(b'\x18')  # Envoie du caractère Ctrl-X (0x18) pour un Soft-Reset
        logging.warning("Aborting the stage (soft-reset). May require a re-homing.")

    def stop(self):
        """
        Stop the stage.
        Note
        ----
        * This sends the "Jog Cancel" command. It immediately cancels the current jog state by a feed hold and
        automatically flushing any remaining jog commands in the buffer. The command is ignored, if not in a JOG state
        or if jog cancel is already invoked and in-process. Grbl will return to the IDLE state or the DOOR state,
        if the safety door was detected as ajar during the cancel.
        * Use the abort command to do a software reset.
        """
        self.serial.write(b"\x85")  # Jog Cancel

    def move(self, x: float = None, y: float = None, z: float = None, speed: float = 500,
             blocking: bool = True) -> None:
        """
        Move the stage to a given work position in mm
        Parameters
        ----------
        x
            X position (mm)
        y
            Y position (mm)
        z
            Z position (mm)
        speed
            Speed (mm/min) (also called feedrate in grbl)
        blocking
            If True, the method will only return once the move has ended.
        """
        logging.info("Moving to an absolute work position")
        assert x is not None or y is not None or z is not None, "At least one of x, y, z or speed must be set"

        # Preparing the gcode
        gcode = ['G90'] # Absolute move

        # Adding target position
        if x is not None:
            gcode.append(f"X{x}")
        if y is not None:
            gcode.append(f"Y{y}")
        if z is not None:
            gcode.append(f"Z{z}")

        # Adding the feedrate in mm/min
        gcode.append(f"F{speed}")

        # Sending the command
        command = "$J=" + " ".join(gcode)  # Run a job motion
        self.send_command(command)

        if blocking:
            self.wait_for_movement_completion()

    def move_relative(self, dx: float = None, dy: float = None, dz: float = None, speed: float = 500,
                      blocking: bool = True):
        """
        Move the stage by a distance relative to the current position
        ----------
        dx
            X distance (mm)
        dy
            Y distance (mm)
        dz
            Z distance (mm)
        speed
            Speed (mm/min) (also called feedrate in grbl)
        blocking
            If True, the method will only return once the move has ended.
        """
        logging.info("Performing a relative move")
        assert dx is not None or dy is not None or dz is not None, "At least one of dx, dy, dz or speed must be set"

        # Preparing the gcode
        gcode = ["G91"]  # This is an incremental move

        # Adding target position
        if dx is not None:
            gcode.append(f"X{dx}")
        if dy is not None:
            gcode.append(f"Y{dy}")
        if dz is not None:
            gcode.append(f"Z{dz}")

        # Adding the feedrate in mm/min
        gcode.append(f"F{speed}")

        # Sending the command
        command = "$J=" + " ".join(gcode)  # Run a job motion
        self.send_command(command)

        if blocking:
            self.wait_for_movement_completion()

    def wait_for_movement_completion(self):
        """ Waits for a move to complete before returning"""

        idle_counter = 0
        while True:
            report = self.status_report
            if report['state'] != 'ok':
                if report['state'] == 'Idle':
                    idle_counter += 1
            if idle_counter > 10:
                break

    @property
    def position(self):
        """X,Y,Z stage (machine) position in mm"""
        position = self.status_report["pos_mm"]  # Position in machine coordinates
        position = [x - x0 for x, x0 in zip(position, self.origin_position)]
        return position

    @property
    def gcode_parameters(self) -> dict:
        """Gcode Parameters"""
        gcode_parameters = dict()
        response = self.send_command("$#")
        for elem in response:
            elem = elem.replace("[", "").replace("]", "").split(":")
            key = elem[0]
            values = [float(x) for x in elem[1].split(",")]
            if key == "PRB":
                values.append(int(elem[2]))
            gcode_parameters[key] = values
        return gcode_parameters

    @property
    def gcode_parser_state(self) -> list:
        """Gcode parser state"""
        gcode_parser_state = self.send_command("$G").split(":")[1].split(" ")
        return gcode_parser_state

    @property
    def grbl_settings(self) -> dict:
        """GRBL Settings"""
        grbl_settings = dict()
        response = self.send_command("$$")
        for elem in response:
            key, value = elem.split("=")
            grbl_settings[key] = {"value": value, "description": GRBL_SETTINGS_DEFINITIONS.get(key, "N/A")}
        return grbl_settings

    @property
    def status_report(self) -> dict:
        """Get the GRBL status report"""
        foo = self.send_command("?")

        # Split the status report
        foo = foo.replace("<", "").replace(">", "").split("|")
        report = dict()
        report['state'] = foo[0]
        for elem in foo[1:]:
            key, value = elem.split(":")
            if key == "MPos":
                value = [float(x) for x in value.split(",")]
                report["pos_mm"] = value
            elif key == "FS":
                value = [float(x) for x in value.split(",")]
                report["feedrate_mm/s"] = value[0]
                report["spindlespeed_mm/s"] = value[1]
            else:
                report[key] = value
        return report

    @property
    def current_origin(self):
        """Get the current origin machine coordinate position"""
        raise NotImplementedError("This property is not implemented yet")


class SOCTXYZStage(PDVStageController):
    def __init__(self):
        super().__init__(config['soct-stage-xyz']['com_port'])
        self.connect()
        # Configure the stage
        self.configure(config['soct-stage-xyz'])


class PLIXYZStage(PDVStageController):
    def __init__(self):
        super().__init__(config['pli-stage-xyz']['com_port'])
        self.connect()
        # Configure the stage
        self.configure(config['pli-stage-xyz'])


class PLIRotStage(PDVStageController):
    def __init__(self):
        super().__init__(config['pli-stage-rot']['com_port'])
        self.connect()

        # Configure the stage
        self.configure(config['pli-stage-rot'])



    @property
    def position(self):
        """Top and Bottom rotation in degrees. The third element is unused"""
        position = self.status_report["pos_mm"]  # Position in machine coordinates
        position = [x - x0 for x, x0 in zip(position, self.origin_position)]
        return position





    # TODO : Overload the position and move methods to change the parameters name for theta and phi
    # FIXME: top and bottom rotation are not in the same directions


def test_stage():
    # Connect
    stage = PDVStageController()
    stage.connect()
    print("Initial Position:", stage.position)
    print(stage.status_report)

    # Testing the homing
    stage.homing()
    print(stage.status_report)

    # Read the setting
    print(stage.grbl_settings)
    print("Final position:", stage.position)

    stage.disconnect()


if __name__ == '__main__':
    test_stage()
