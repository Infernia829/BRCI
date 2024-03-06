import os

from BRAPIF import *

# ------------------------------------------------------------
# DEFAULT VARIABLES AND SETUP
# ------------------------------------------------------------

# Setup variables
version = "C2"

# Important variables
_cwd = os.path.dirname(os.path.realpath(__file__))

# Temporary Variables
# No Temporary Variables.


# ------------------------------------------------------------
# DATA WRITING
# ------------------------------------------------------------


# Return all data about specified brick
def create_brick(brick: str):
    return br_brick_list[brick]


# What am I supposed to comment here?
class BRAPI:

    # Getting all values. Do I have to comment that too?
    def __init__(self,
                 bricks=None,
                 project_folder_directory='',
                 project_name='',
                 write_blank=False,
                 project_display_name='',
                 file_description=''):

        # I'm not commenting this either.
        self.project_folder_directory = project_folder_directory
        self.project_name = project_name
        self.write_blank = write_blank
        self.project_display_name = project_display_name
        self.file_description = file_description
        if bricks is None:
            bricks = []
        self.bricks = bricks


    # Creating more variables
    # In project path
    @property
    def in_project_folder_directory(self):
        return os.path.join(self.project_folder_directory, self.project_name)

    # Calculate brick count
    @property
    def brick_count(self):
        return len(self.bricks)

    # Calculate vehicle size
    @property
    def vehicle_size(self):
        # TODO : CALCULATE SIZE
        return [1, 2, 3]

    # Calculate vehicle weight
    @property
    def vehicle_weight(self):
        # TODO : CALCULATE WEIGHT
        return 0.1

    # Calculate vehicle worth
    @property
    def vehicle_worth(self):
        # TODO : CALCULATE WORTH
        return 0.2

    # Adding bricks to the brick list
    def add_brick(self, brick_name, new_brick):
        self.bricks.append([str(brick_name), new_brick])


    # Removing bricks from the brick list
    def remove_brick(self, brick_name):
        self.bricks = [sublist for sublist in self.bricks if sublist[0] != str(brick_name)]


    # Updating a currently existing brick
    def update_brick(self, brick_name, new_brick):
        self.remove_brick(brick_name)
        self.add_brick(brick_name, new_brick)


    # Used to create directory for file generators
    def ensure_project_directory_exists(self):
        os.makedirs(os.path.dirname(os.path.join(self.in_project_folder_directory, self.project_name)), exist_ok=True)


    # Writing preview.png
    def write_preview(self):

        # Create folder if missing
        self.ensure_project_directory_exists()

        # Copy saved image to the project folders.
        copy_file(os.path.join(_cwd, "Resources", "icon_compressed_reg.png"),
                  os.path.join(self.in_project_folder_directory, "Preview.png"))


    # Writing metadata.brm file
    def write_metadata(self):

        # Create folder if missing
        self.ensure_project_directory_exists()

        # Write blank file for metadata (if desired)
        if self.write_blank:
            blank_metadata = open(os.path.join(self.in_project_folder_directory, "MetaData.brm"), "x")
            blank_metadata.close()

        # Otherwise write working metadata file
        else:
            with open(os.path.join(self.in_project_folder_directory, "MetaData.brm"), 'wb') as metadata_file:

                # Writes Carriage Return char
                metadata_file.write(unsigned_int(13, 1))

                # Write all necessary information for the file name
                line_feed_file_name = (((self.project_name.replace("\\n", "\n")).encode('utf-16'))
                                       .replace(b'\x0A\x00',b'\x0D\x00\x0A\x00')).decode('utf-16')
                metadata_file.write(signed_int(-len(line_feed_file_name), 2))
                metadata_file.write(bin_str(line_feed_file_name)[2:])

                # Write all necessary information for the file description
                watermarked_file_description = f"Created using BR-API.\n" \
                                               f"BR-API Version {version}.\n\n" \
                                               f"Description:\n{self.file_description}."
                watermarked_file_description = (
                    ((watermarked_file_description.replace("\\n", "\n")).encode('utf-16'))
                    .replace(b'\x0A\x00',b'\x0D\x00\x0A\x00')).decode('utf-16')
                metadata_file.write(signed_int(-len(watermarked_file_description), 2))
                metadata_file.write(bin_str(watermarked_file_description)[2:])

                # Write all necessary information for the 4 additional values : Bricks, Size, Weight and Monetary Value
                metadata_file.write(signed_int(self.brick_count, 2))
                metadata_file.write(bin_float(self.vehicle_size[0], 4))
                metadata_file.write(bin_float(self.vehicle_size[1], 4))
                metadata_file.write(bin_float(self.vehicle_size[2], 4))
                metadata_file.write(bin_float(self.vehicle_weight, 4))
                metadata_file.write(bin_float(self.vehicle_worth, 4))

                # Writes the author. We don't want it to be listed, so we write invalid data.
                metadata_file.write(bytes.fromhex('FFFFFFFFFFFFFFFF'))

                # I have no fucking clue of what I'm writing but hey it's something right?
                metadata_file.write(bytes.fromhex("14686300000000B034B6C7382ADC08E079251F392ADC08"))

                # Writing tags                                                                                          TODO Broken
                metadata_file.write(unsigned_int(3, 1))
                for i in range(3):
                    metadata_file.write(unsigned_int(5, 1))
                    metadata_file.write(small_bin_str("Other"))


    # Writing Vehicle.brv
    def write_brv(self):

        # Create folder if missing
        self.ensure_project_directory_exists()

        # Write blank file for vehicle (if desired)
        if self.write_blank:
            blank_brv = open(os.path.join(self.in_project_folder_directory, "Vehicle.brv"), "x")
            blank_brv.close()

        # Otherwise write working vehicle file
        else:
            with open(os.path.join(self.in_project_folder_directory, "Vehicle.brv"), 'wb') as brv_file:

                brv_file.write(unsigned_int(13, 1))
                brv_file.write(unsigned_int(self.brick_count, 2))


        print(self.bricks)


@dataclass
class BrickInput:

    brick_input_type: str
    brick_input: any


"""
# Try it out
data = BRAPI()
data.project_name = 'test_project'
data.project_display_name = 'My Project'
data.project_folder_directory = os.path.join(_cwd, 'Projects')

print(data.project_folder_directory)

data.write_preview()
data.write_metadata()
"""

"""
# Doesnt matter.
my_test_brick = create_brick('Switch_1sx1sx1s')
data.add_brick('my_test_brick', my_test_brick)
print(my_test_brick)
print(data.bricks)
"""