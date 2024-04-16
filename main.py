import os
# from warnings import warn as raise_warning

from BRAPIF import *

# Note : every time you see unsigned_int() / signed_int() / bin_float(), byte_len * 8 is the number of bits.

# TODO Add more jokes in comments because they're pretty annoying.
# TODO Comment each variable to specify their content & classes for rust translation.
# TODO Add all bricks in br_brick_list
# TODO Calculate vehicle_size, vehicle_weight and vehicle_worth
# TODO Find another way to make Brick Inputs. (Perhaps they should work and I'm just an idiot?)
# TODO Finish Appendix System
# TODO Implement Brick Loading (IDEA : Exclusively load user appendix)?

# ------------------------------------------------------------
# DEFAULT VARIABLES AND SETUP
# ------------------------------------------------------------



# Setup variables
version: str = "C21"  # String, This is equivalent to 3.__ fyi

# Important variables
_cwd = os.path.dirname(os.path.realpath(__file__))  # File Path

# Colors

from os import system as os_system
os_system('color')

# Fight to the end about the class name fr 
class clr:
    reset = '\x1b[0m' # Reset code
    red = '\x1b[31m'
    blue = '\x1b[34m'
    green = '\x1b[32m'
    yellow = '\x1b[33m'
    purple = '\x1b[35m'
    cyan = '\x1b[36m'
    white = '\x1b[37m'
    black = '\x1b[30m'
    light_blue = '\x1b[94m'
    light_green = '\x1b[92m'
    light_red = '\x1b[91m'
    light_purple = '\x1b[95m'
    light_white = '\x1b[97m'
    light_black = '\x1b[90m'
    light_cyan = '\x1b[96m'
    light_yellow = '\x1b[93m'
    bold = '\x1b[1m'
    underline = '\x1b[4m'
    italic = '\x1b[3m'
    reverse = '\x1b[7m'
    strikethrough = '\x1b[9m'
    remove_color = '\x1b[39m'
    remove_bold = '\x1b[22m'
    remove_underline = '\x1b[24m'
    remove_italic = '\x1b[23m'
    remove_reverse = '\x1b[27m'
    remove_strikethrough = '\x1b[29m'
    bg_red = '\x1b[41m'
    bg_green = '\x1b[42m'
    bg_blue = '\x1b[44m'
    bg_yellow = '\x1b[43m'
    bg_black = '\x1b[40m'
    bg_white = '\x1b[47m'
    bg_light_red = '\x1b[101m'
    bg_light_green = '\x1b[102m'
    bg_light_blue = '\x1b[104m'
    bg_light_yellow = '\x1b[103m'
    bg_light_black = '\x1b[100m'
    bg_light_white = '\x1b[107m'
    bg_purple = '\x1b[45m'
    bg_light_purple = '\x1b[105m'
    bg_cyan = '\x1b[46m'
    bg_light_cyan = '\x1b[106m'
    info = f'{reverse}{light_blue}[INFO]{remove_reverse}'
    success = f'{reverse}{light_green}[SUCCESS]{remove_reverse}'
    error = f'{reverse}{light_red}[ERROR]'
    warning = f'{reverse}{yellow}[WARNING]'
    debug = f'{reverse}{light_purple}[DEBUG]{remove_reverse}'
    test = f'{reverse}{light_cyan}[TEST]{remove_reverse}'

    @staticmethod
    def error_with_header(header, text):
        print(f"{clr.error} {header}{clr.remove_reverse} \n{text}")

    @staticmethod
    def warning_with_header(header, text):
        print(f"{clr.warning} {header}{clr.remove_reverse} \n{text}")




from builtins import print as print_ins
# Override the built-in print function
def print(*args, end='\n', reset_color=True, **kwargs):
    # I removed this comment because my IDE complained about it containing a typo (there was none :bob_troll:)
    if reset_color: print_ins(*args, end=f"{end}{clr.reset}", **kwargs)
    else: print_ins(*args, end=f"{end}", **kwargs)

# ------------------------------------------------------------
# DATA WRITING
# ------------------------------------------------------------


# Return all data about specified brick
#def create_brick(brick: str):
    #return br_brick_list[brick].copy()

# pain

def create_brick(brick: str, brick_properties: dict = None) -> dict:
    if brick_properties is None:
        brick_properties = {}
    return br_brick_list[brick].copy() | brick_properties


# Brick Rigs API Class
class BRAPI:

    # Grab values
    def __init__(self,
                 bricks=None,
                 project_folder_directory='',
                 project_name='',
                 write_blank=False,
                 project_display_name='',
                 file_description='',
                 debug_logs=None,
                 user_appendix=b''):

        # Set each self.x variable to their __init__ counterparts
        self.project_folder_directory = project_folder_directory  # Path
        self.project_name = project_name  # String
        self.write_blank = write_blank  # Boolean
        self.project_display_name = project_display_name  # String (in-game name (.brm))
        self.file_description = file_description  # String (The description of the file (.brm))
        if bricks is None:  # List (If unspecified, create an empty list)
            bricks = [] # Initialize bricks
        self.bricks = bricks # List (Of bricks)
        if debug_logs is None:
            debug_logs = []
        self.debug_logs = debug_logs # List of logs to print
        self.user_appendix = user_appendix # List (User appendix)


    # Creating more variables
    # In project path
    @property
    def in_project_folder_directory(self): # String
        return os.path.join(self.project_folder_directory, self.project_name)

    # Calculate brick count
    @property
    def brick_count(self): # 16 Bit integer
        return len(self.bricks)

    # Calculate vehicle size
    @property
    def vehicle_size(self): # List of 3 32-bit float
        # TODO : CALCULATE SIZE
        return [1, 2, 3]

    # Calculate vehicle weight
    @property
    def vehicle_weight(self): # 32 bit float
        # TODO : CALCULATE WEIGHT
        return 0.1

    # Calculate vehicle worth
    @property
    def vehicle_worth(self): # 32 bit float
        # TODO : CALCULATE WORTH
        return 0.2 # I wonder if this will make it 0.2 in-game? Or does BR calculate the price itself?

    # Adding bricks to the brick list
    def add_brick(self, brick_name: str, new_brick: dict):
        self.bricks.append([str(brick_name), new_brick]) # TODO : CHECK IF NAME IS INVALID (probably by using BRAPIF)

        return self


    # Removing bricks from the brick list
    def remove_brick(self, brick_name: str):

        self.bricks = [sublist for sublist in self.bricks if sublist[0] != str(brick_name)]

        return self


    # Updating a currently existing brick
    def update_brick(self, brick_name: str, new_brick: dict):
        self.remove_brick(brick_name)
        self.add_brick(brick_name, new_brick)

        return self


    def ensure_valid_variable_type(self, variable_name: str, occured_when: str) -> None:
        match variable_name:
            case 'write_blank':
                if not isinstance(self.write_blank, bool):
                    clr.error_with_header("Invalid write_blank type.",
                        f"Whilst {occured_when}, write_blank was found not to be a boolean, it was instead a "
                        f"{type(self.write_blank).__name__}.\nIt is now set to False.")
                    self.write_blank = False
            case 'bricks_len':
                if len(self.bricks) > 65535:
                    clr.error_with_header("Too many bricks.",
                        f"Whilst {occured_when}, the length of the list of bricks was found to exceed 65,535.\n"
                        f"Therefore, the last {len(self.bricks)-65535 :,} brick(s) were removed. 65,535 bricks left.")
                    self.bricks = self.bricks[:65535]
            case 'logs':
                logs_whitelist_list: list[str] = ['time', 'bricks']
                invalid_logs_list: list[str] = []
                for log_request_str in self.debug_logs:
                    if not log_request_str in logs_whitelist_list:
                        invalid_logs_list.append(log_request_str)
                if invalid_logs_list:
                    invalid_logs_str: str =  ', '.join(invalid_logs_list)
                    logs_whitelist_str: str = ', '.join(logs_whitelist_list)
                    clr.warning_with_header("Unknown log(s) type requested.",
                        f"Whilst {occured_when}, the following log(s) type requested were found to be invalid: "
                        f"{invalid_logs_str}.\nYou may instead use the following: {logs_whitelist_str}.")



    # Used to create directory for file generators
    def ensure_project_directory_exists(self):

        # Verify for invalid inputs
        if not os.path.exists(self.project_folder_directory):

            raise FileNotFoundError(f'Unable to find the project\'s folder ({self.project_folder_directory})')

        os.makedirs(os.path.dirname(os.path.join(self.in_project_folder_directory, self.project_name)), exist_ok=True)


    # Writing preview.png
    def write_preview(self):

        _write_preview_regular_image_path = os.path.join(_cwd, 'Resources', 'icon_beta.png') # Path

        # Create folder if missing
        self.ensure_project_directory_exists()

        # Verify the image exists.
        if not os.path.exists(_write_preview_regular_image_path):

            clr.error_with_header("Image not found", "Whilst writing Preview.png, we were unable to"
                                                         "find BR-API default image. Please retry.")

        # Copy saved image to the project folders.
        else:
            if os.path.exists(os.path.join(self.in_project_folder_directory, "Preview.png")):
                clr.warning_with_header("Dest Code Activated, Project Overwritten", "If you are seeing this, Destiny's Debug code has triggered. This means that your project has been overwritten without errors.")
                os.remove(os.path.join(self.in_project_folder_directory, "Preview.png"))

            copy_file(os.path.join(_write_preview_regular_image_path),
                os.path.join(self.in_project_folder_directory, "Preview.png"))

    # Writing metadata.brm file
    def write_metadata(self):

        # Create folder if missing
        self.ensure_project_directory_exists()
        self.ensure_valid_variable_type('write_blank', 'writing MetaData.brm')
        self.ensure_valid_variable_type('bricks_len', 'writing MetaData.brm')

        # Write blank file for metadata (if desired)
        if self.write_blank:

            with open(os.path.join(self.in_project_folder_directory, "MetaData.brm"), "x"):
                pass

        # Otherwise write working metadata file
        else:
            with open(os.path.join(self.in_project_folder_directory, "MetaData.brm"), 'wb') as metadata_file:

                # Writes Carriage Return char
                metadata_file.write(unsigned_int(13, 1))

                # Write all necessary information for the file name
                line_feed_file_name = (((self.project_display_name.replace("\\n", "\n")).encode('utf-16'))
                                       .replace(b'\x0A\x00', b'\x0D\x00\x0A\x00')).decode('utf-16') # String
                metadata_file.write(signed_int(-len(line_feed_file_name), 2))
                metadata_file.write(bin_str(line_feed_file_name)[2:])

                # Write all necessary information for the file description
                watermarked_file_description = f"Created using BR-API (Version {version}).\n" \
                                               f"Join our discord for more information : [INVITE LINK]\n\n" \
                                               f"Description:\n{self.file_description}." # String
                watermarked_file_description = (
                    ((watermarked_file_description.replace("\\n", "\n")).encode('utf-16'))
                    .replace(b'\x0A\x00', b'\x0D\x00\x0A\x00')).decode('utf-16') # String
                metadata_file.write(signed_int(-len(watermarked_file_description), 2))
                metadata_file.write(bin_str(watermarked_file_description)[2:])

                # Write all necessary information for the 4 additional values : Bricks, Size, Weight and Monetary Value
                metadata_file.write(unsigned_int(self.brick_count, 2))
                metadata_file.write(bin_float(self.vehicle_size[0], 4))
                metadata_file.write(bin_float(self.vehicle_size[1], 4))
                metadata_file.write(bin_float(self.vehicle_size[2], 4))
                metadata_file.write(bin_float(self.vehicle_weight, 4))
                metadata_file.write(bin_float(self.vehicle_worth, 4))

                # Writes the author. We don't want it to be listed, so we write invalid data.
                metadata_file.write(bytes.fromhex('FFFFFFFFFFFFFFFF')) # What if a steam ID someday reaches this limit? Never!

                # I have no fucking clue of what I'm writing but hey it's something right?
                metadata_file.write(bytes.fromhex("14686300000000B034B6C7382ADC08E079251F392ADC08")) # Peak programming. TODO Figure out what the fuck we're writing here


                # Write a function for a very specific and stupid purpose
                def write_tags_to_file(tag1: str = "Other", tag2: str = "Other", tag3: str = "Other"):
                    metadata_file.write(unsigned_int(3, 1))
                    for i in range(3):
                        metadata_file.write(unsigned_int(5, 1))
                        metadata_file.write(small_bin_str(locals()[f"tag{i+1}"])) # "locals()" returns the dict of all variables in the current scope
                        # Trying to modify said dict will actually add a new variable or change an existing one. I don't know why, since it is returning the *current* variables.


                # Writing tags                                                                                          FIXME
                write_tags_to_file() # TODO: Add a way to input tags. For now, they are all "Other"



    # Sharing some variables from writing vehicle.brv to the rest of the class
    bricks_writing = []
    inverted_property_key_table = {}
    id_assigned_property_table = {}
    brapi_appendix: list = []



    # Writing Vehicle.brv
    def write_brv(self):

        self.ensure_project_directory_exists()

        # Verify self.write_blank is valid.
        self.ensure_valid_variable_type('write_blank', 'writing Vehicle.brv')

        # Write blank file for vehicle (if desired)
        if self.write_blank:
            blank_brv = open(os.path.join(self.in_project_folder_directory, "Vehicle.brv"), "x")
            blank_brv.close()

        # Otherwise write working vehicle file
        else:

            # Show generation time if debug logs
            from time import perf_counter
            previous_time = perf_counter()
            begin_time = perf_counter()

            def brv_brick_types(bricks: list, debug: bool = False) -> list:
                brick_types_f = list(set(item[1]['gbn'] for item in bricks))
                if debug:
                    print(f'{clr.debug} Brick Types......... : {brick_types_f}')
                return brick_types_f

            # FIXME DESTINY
            # Add missing properties. Only made for BrickInput() but there may be more stuff later on
            def add_missing_properties(bricks: list, debug: bool = False) -> None:
                print("CALLED")
                for brick_mp in bricks:
                    print("FOR BRICK")
                    properties_to_add: dict = {}
                    properties_to_remove: dict = {}
                    for property_key_mp, property_value_mp in brick_mp[1].items():
                        print("FOR PROPERTY")
                        print(type(property_value_mp))
                        if isinstance(property_value_mp, BrickInput):
                            print("DETECTED")
                            #print(f"{clr.debug} property_value_mp.properties() : {property_value_mp.properties()}")
                            #print(f"{clr.debug} properties_to_add : {properties_to_add}")
                            prop_mp_temp = property_value_mp.properties()
                            #print(f"{clr.debug} prop_mp_temp : {prop_mp_temp}")
                            properties_to_add.update(prop_mp_temp)
                            print(f"{clr.debug} properties_to_remove : {properties_to_remove}")
                            print(f"{clr.debug} property_key_mp : {property_key_mp}")
                            properties_to_remove.update(property_key_mp)
                    brick_mp[1].pop(properties_to_remove)
                    #print(f"{clr.debug} properties_to_add[0] : {properties_to_add[0]}")
                    brick_mp[1].update(properties_to_add)
                if debug:
                    print(f'{clr.debug} Modified Brick List. : {bricks}')


            # Verify if there are too many bricks
            self.ensure_valid_variable_type('bricks_len', 'writing Vehicle.brv')
            self.ensure_valid_variable_type('logs', 'writing Vehicle.brv')

            with open(os.path.join(self.in_project_folder_directory, "Vehicle.brv"), 'wb') as brv_file:


                self.bricks_writing = self.bricks.copy()

                # Writes Carriage Return char
                brv_file.write(unsigned_int(13, 1))
                # Write brick count
                brv_file.write(unsigned_int(len(self.bricks_writing), 2))

                # Add all missing properties, notably inputs.
                add_missing_properties(self.bricks_writing, 'bricks' in self.debug_logs)

                if 'time' in self.debug_logs:
                    print(f'{clr.debug} Time: Missing Properties.. : {perf_counter() - previous_time :.6f} seconds')

                # Get the different bricks present in the project
                brick_types = brv_brick_types(self.bricks_writing, 'bricks' in self.debug_logs) # List

                if 'time' in self.debug_logs:
                    print(f'{clr.debug} Time: Brick Types......... : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                # Write the number of different brick types
                brv_file.write(unsigned_int(len(brick_types), 2))

                # [ Getting rid of all properties that are set to the default value for each brick ]
                # Brick list filtering variables
                temp_iebl = []  # List of lists containing an integer and a list containing a dictionary and integers
                safe_property_list: list[str] = ['gbn', 'Position', 'Rotation']

                # Defining bricks
                w_current_brick_id = 0  # 16 bit
                string_name_to_id_table = {}
                property_table = {}

                # List Properties
                for current_brick in self.bricks_writing:
                    # Add all bricks without including data
                    temp_iebl.append([w_current_brick_id, [{}, {}]])
                    string_name_to_id_table[current_brick[0]] = w_current_brick_id
                    w_current_brick_id += 1

                    # For each data for each brick
                    for p_del_current_key, p_del_current_value in current_brick[1].items():
                        # Accept if it's in the safe list (list which gets whitelisted even if default value is identical)
                        if p_del_current_key in safe_property_list:
                            temp_iebl[-1][1][0][p_del_current_key] = p_del_current_value
                        # Otherwise regular process: if not default, get rid of it
                        elif p_del_current_value != br_brick_list[current_brick[1]['gbn']][p_del_current_key]:
                            temp_iebl[-1][1][1][p_del_current_key] = p_del_current_value
                            # Make sure key in the dict exists
                            property_table.setdefault(p_del_current_key, [])
                            # Setup property table
                            if p_del_current_value not in property_table[p_del_current_key]:
                                property_table[p_del_current_key].append(p_del_current_value)

                if 'time' in self.debug_logs:
                    print(f'{clr.debug} Time: ID Assigning........ : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()


                # Setup property ids
                w_current_property_id: int = 0  # 32 bit
                w_property_count: int = 0 # 32 bit
                property_key_table: dict = {}
                w_property_key_num: int = 0

                # Give IDs to all values in var 'id_assigned_property_table'
                for property_value_key, property_value_value in property_table.items():

                    self.id_assigned_property_table = self.id_assigned_property_table | {property_value_key: {}}

                    for pvv_value in property_value_value:

                        self.id_assigned_property_table[property_value_key] = self.id_assigned_property_table[property_value_key] | {w_current_property_id: pvv_value}
                        w_current_property_id += 1
                        w_property_count += 1

                    property_key_table = property_key_table | {property_value_key: w_property_key_num}
                    self.inverted_property_key_table = self.inverted_property_key_table | {w_property_key_num: property_value_key}
                    w_property_key_num += 1
                    w_current_property_id = 0


                if 'time' in self.debug_logs:
                    print(f'{clr.debug} Time: Prop. ID Assigning.. : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                # Give IDs
                temp_bricks_writing: list = []

                for current_brick in range(len(self.bricks_writing)):

                    temp_bricks_writing += [[temp_iebl[current_brick][0], [temp_iebl[current_brick][1][0], []]]]

                    # Give Property IDs, Brick Type IDs
                    for current_property, current_property_value in temp_iebl[current_brick][1][1].items():

                        # Find what the id is
                        for key, value in self.id_assigned_property_table[current_property].items():
                            if value == current_property_value:
                                found_key: int = int(key)

                        # Giving IDs
                        temp_bricks_writing[-1][1][1].append([property_key_table[current_property], found_key])

                    # Giving Brick Type IDs
                    temp_bricks_writing[-1][1][0]['gbn'] = brick_types.index(temp_bricks_writing[-1][1][0]['gbn'])

                if 'time' in self.debug_logs:
                    print(f'{clr.debug} Time: Temp Bricks Writing. : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                # Insert n-word here

                # Bricks Writing is ready to be updated!
                self.bricks_writing = temp_bricks_writing.copy()

                if 'time' in self.debug_logs:
                    print(f'{clr.debug} Time: Bricks Writing...... : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()


                # Debug
                if 'bricks' in self.debug_logs:
                    print(f'{clr.debug} Identical Excluded Brick L : {temp_iebl}')
                    print(f'{clr.debug} Property Table............ : {property_table}')
                    print(f'{clr.debug} ID Assigned Property Table : {self.id_assigned_property_table}')
                    print(f'{clr.debug} Brick Properties Writing.. : {self.bricks_writing}')
                    print(f'{clr.debug} String Name to ID Table... : {string_name_to_id_table}')
                    print(f'{clr.debug} Brick Types............... : {brick_types}')
                    print(f'{clr.debug} Property Key Table........ : {property_key_table}')
                    print(f'{clr.debug} Inverted Property Key Tbl. : {self.inverted_property_key_table}')

                # Write how many properties there are
                brv_file.write(unsigned_int(len(property_table), 2))


                # Write each brick type
                for brick_type in brick_types:
                    brv_file.write(unsigned_int(len(brick_type), 1))
                    brv_file.write(small_bin_str(brick_type))

                if 'time' in self.debug_logs:
                    print(f'{clr.debug} Time: Write Brick Types... : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()

                temp_spl: bytes = b''

                # Write properties
                for property_type_key, property_type_value in property_table.items():
                    # Writing keys
                    brv_file.write(unsigned_int(len(property_type_key), 1))
                    brv_file.write(small_bin_str(property_type_key))
                    # Number of values
                    brv_file.write(unsigned_int(len(property_type_value), 2))

                    # Summing values
                    property_length_precised: bool = False
                    for pt_c_val in property_type_value: # property_table_current_value
                        if property_type_key not in br_special_property_instance_list:


                            # If it's an integer (uint 16 bit by default)
                            if type(pt_c_val) == int:  # This is because it fucks around when its bool as bool is a subtype of int
                                temp_spl += unsigned_int(pt_c_val, 2)


                            # If it's a float (float 32 bit by default)
                            if isinstance(pt_c_val, float):
                                temp_spl += bin_float(pt_c_val, 4)


                            # If it's a bool
                            if isinstance(pt_c_val, bool):
                                temp_spl += unsigned_int(int(pt_c_val), 1)


                            # If it's a string (converting to utf-16)
                            if isinstance(pt_c_val, str):
                                temp_spl += signed_int(-len(pt_c_val), 2)
                                temp_spl += bin_str(pt_c_val)
                        else:
                            match br_special_property_instance_list[property_type_key]:
                                case 'INT8':
                                    temp_spl += unsigned_int(pt_c_val, 1)
                                case '6xINT2':
                                    temp_w_spl_connector = pt_c_val[0] + (pt_c_val[1]<<2) + (pt_c_val[2]<<4) + (pt_c_val[3]<<6) + (pt_c_val[4]<<8) + (pt_c_val[5]<<10)
                                    temp_spl += unsigned_int(temp_w_spl_connector, 2)
                                case '3xINT16':
                                    temp_spl += unsigned_int(pt_c_val[0], 2)
                                    temp_spl += unsigned_int(pt_c_val[1], 2)
                                    temp_spl += unsigned_int(pt_c_val[2], 2)
                                case '3xINT8':
                                    temp_spl += unsigned_int(pt_c_val[0], 1)
                                    temp_spl += unsigned_int(pt_c_val[1], 1)
                                    temp_spl += unsigned_int(pt_c_val[2], 1)
                                case '4xINT8':
                                    temp_spl += unsigned_int(pt_c_val[0], 1)
                                    temp_spl += unsigned_int(pt_c_val[1], 1)
                                    temp_spl += unsigned_int(pt_c_val[2], 1)
                                    temp_spl += unsigned_int(pt_c_val[3], 1)

                        if not property_length_precised :
                            property_length = len(temp_spl)
                            property_length_precised = True


                    brv_file.write(unsigned_int(len(temp_spl), 4))
                    brv_file.write(temp_spl)

                    # Indicating property length if there's more than one property value.
                    if len(property_type_value) > 1:
                        brv_file.write(unsigned_int(property_length, 2))

                    temp_spl: bytes = b''  # Reset

                if 'time' in self.debug_logs:
                    print(f'{clr.debug} Time: Write Properties.... : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()


                # WRITING BRICKS
                brick_data_writing: bytes = b''


                for current_brick in self.bricks_writing:

                    # Writing Brick Type
                    brv_file.write(unsigned_int(current_brick[1][0]['gbn'], 2))
                    # Getting ready to list properties
                    brick_data_writing += unsigned_int(len(current_brick[1][1]), 1)
                    for current_property in current_brick[1][1]:
                        brick_data_writing += unsigned_int(current_property[0], 2)
                        brick_data_writing += unsigned_int(current_property[1], 2)
                    # Getting ready to write position and rotation
                    brick_data_writing += bin_float(current_brick[1][0]['Position'][0], 4)
                    brick_data_writing += bin_float(current_brick[1][0]['Position'][1], 4)
                    brick_data_writing += bin_float(current_brick[1][0]['Position'][2], 4)
                    # Note sure why its out of order in the brv. Whatever
                    brick_data_writing += bin_float(current_brick[1][0]['Rotation'][0], 4)
                    brick_data_writing += bin_float(current_brick[1][0]['Rotation'][1], 4)
                    brick_data_writing += bin_float(current_brick[1][0]['Rotation'][2], 4)

                    # Writing
                    brv_file.write(unsigned_int(len(brick_data_writing), 4))
                    brv_file.write(brick_data_writing)

                    # Reset
                    brick_data_writing = b''

                brv_file.write(b'\x00\x00')

                if 'time' in self.debug_logs:
                    print(f'{clr.debug} Time: Write Bricks........ : {perf_counter() - previous_time :.6f} seconds')
                    previous_time = perf_counter()


                #  BR-API & USER APPENDIX


                brv_watermark = f'File written with BR-API version {version}. Join our discord to learn more: sZXaESzDd9'
                self.brapi_appendix.append(small_bin_str(brv_watermark))


                for brapi_individual_appendix in self.brapi_appendix:
                    brv_file.write(unsigned_int(len(brapi_individual_appendix), 4))
                    brv_file.write(brapi_individual_appendix)

                if 'time' in self.debug_logs:
                    print(f'{clr.debug} Time: Write Appendix...... : {perf_counter() - previous_time :.6f} seconds')
                    print(f'{clr.debug} Time: Total............... : {perf_counter() - begin_time :.6f} seconds')

    def debug_print(self, summary_only=False, write=True, print_bricks=False):

        def named_spacer(name: str):
            return '=== ' + name + ' ' + '=' * (95 - len(name))

        spacer = '█' * 100

        str_to_write = ''

        # PRINTING GENERAL INFORMATION
        str_to_write += spacer + '\n'
        str_to_write += named_spacer("PROJECT INFORMATION") + '\n'
        str_to_write += f"PROJECT FOLDER: {self.in_project_folder_directory}\n"
        str_to_write += f"PROJECT NAME: {self.project_display_name!r} [ID: {self.project_name}]\n"
        str_to_write += f"FILE DESCRIPTION: {self.file_description!r}\n"
        str_to_write += f"DEBUG LOGS: {self.debug_logs}\n"
        str_to_write += named_spacer("CREATION INFORMATION") + '\n'
        str_to_write += f"BRICK COUNT: {self.brick_count}\n"
        str_to_write += f"VEHICLE SIZE [X,Y,Z] (CM): {self.vehicle_size}\n"
        str_to_write += f"VEHICLE WEIGHT (KG): {self.vehicle_weight}\n"
        str_to_write += f"VEHICLE WORTH: {self.vehicle_worth}\n"

        # PRINTING BRICKS

        if not summary_only:
            for current_brick in range(len(self.bricks)):

                str_to_write += spacer + '\n'

                # BRICK INFORMATION

                str_to_write += named_spacer('BRICK INFORMATION') + '\n'
                str_to_write += f'BRICK NAME: {self.bricks[current_brick][0]} [ID:{self.bricks_writing[current_brick][0]}]\n'
                str_to_write += (f"BRICK TYPE: {self.bricks[current_brick][1]['gbn']} "
                                 f"[ID: {self.bricks_writing[current_brick][1][0]['gbn']}]\n")
                str_to_write += f"BRICK POS.: {self.bricks[current_brick][1]['Position']}\n"
                str_to_write += f"BRICK ROT.: {self.bricks[current_brick][1]['Rotation']}\n"

                # BRICK PROPERTIES
                str_to_write += named_spacer('BRICK PROPERTIES') + '\n'
                no_properties = True
                for brick_property, brick_property_value in self.bricks_writing[current_brick][1][1]:
                    string_property = self.inverted_property_key_table[brick_property]
                    str_to_write += (f"{string_property}: "
                                     f"{self.id_assigned_property_table[string_property][brick_property_value]}"
                                     f" [ID: {brick_property}, {brick_property_value}]\n")
                    no_properties = False
                if no_properties:
                    str_to_write += "No properties found.\n"

            str_to_write += spacer

        if write:
            with open(os.path.join(self.in_project_folder_directory, "debug_logs.txt"), 'w', encoding='utf-16') as file:
                file.write('DEBUG LOGS\n')
                file.write(str_to_write)

        if print_bricks: print(str_to_write)


# --------------------------------------------------


# Try it out
if __name__ == '__main__':

    # Setting up BR-API
    data = BRAPI()
    data.project_name = 'Input-Channel-Test'
    data.project_display_name = 'Input Channel Test'
    data.project_folder_directory = os.path.join(_cwd, 'Projects') # Do not touch
    data.file_description = 'A test for input channels.'
    data.debug_logs = ['time', 'bricks']
    data.write_blank = None

    def stress_test_run() -> None:
        import random
        for brick_number in range(100_000):
            try:
                test_brick = create_brick(random.choice(list(br_brick_list.keys())))
                temp_test_selected_property = random.choice(list(test_brick.keys()))
                if isinstance(test_brick[temp_test_selected_property], float):
                    test_brick[temp_test_selected_property] = random.uniform(0.0, 1000.0)
                test_brick['Position'] = [random.uniform(0.0, 25000.0), random.uniform(0.0, 25000.0), random.uniform(0.0, 25000.0)]
                test_brick['Rotation'] = [random.uniform(0.0, 360.0), random.uniform(0.0, 360.0), random.uniform(0.0, 360.0)]
                if 'gbn' in test_brick:
                    data.add_brick(str(brick_number), test_brick)
            except KeyError:
                raise KeyError(f'GBN INVALID BRICK')

    def horn_pitch_test() -> None:
        test_pitch = 0.5
        position_x = 0
        hue = 0
        for brick_number_b in range(20):
            test_pitch -= 0.025
            position_x += 10
            hue += 10
            test_current_brick_w = create_brick('DoubleSiren_1x2x1s')
            test_current_brick_w['HornPitch'] = test_pitch
            test_current_brick_w['Position'] = [position_x, 0, 0]
            test_current_brick_w['BrickColor'] = [hue, 255, 255, 255]
            data.add_brick(str(brick_number_b), test_current_brick_w)


    def destiny_s_test() -> None:
        properties = {"Position": [0,0,0], "Rotation": [0,0,0], "BrickColor": [0, 255, 255, 255]}
        switch1 = create_brick('Switch_1sx1sx1s', properties)
        data.add_brick("Switch1", switch1)


    data.write_preview()

    # TODO make an actual default vehicle that wont cause even high end systems to kill themselves when spawned 
    # (or simply just one that doesnt drive people with low end systems away entirely)

    def input_channel_test():
        my_math_brick = create_brick('MathBrick_1sx1sx1s')
        my_math_brick['InputChannelB.InputAxis'] = BrickInput('AlwaysOn', 2_000_000, 'InputChannelB')
        data.add_brick("my_math_brick", my_math_brick)

    input_channel_test()


    print(f"{clr.info} Now generating file.")

    # Writing stuff
    data.write_metadata()
    data.write_brv()
    # data.debug_print(True, False, True) # Prints summary only
    data.debug_print(False, True, False) # Writes all data

    """
    print(f"\n\n{clr.error} An error occurred.")
    print(f"{clr.warning} Press enter to exit.")
    print(f"{clr.info} Press enter to continue.")
    print(f"{clr.success} File successfully generated.")
    print(f"{clr.debug} print(f'" + "{clr.info} Hello world')")
    print(f"{clr.test} Something\n\n")

    clr.error_with_header("Your creation contains too many bricks.", "Brick Rigs limit all creations to 65,535 bricks (16 bit unsigned integer limit).\nYour creation contains 68,194 bricks. 2,649 bricks were removed.")
    clr.warning_with_header("You suck", "And you will never ever get bitches\nBecause you're gay")=)
    
    input(f'\n\n\nwait')
    """