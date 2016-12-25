from opentrons import robot
from opentrons import containers, instruments
from dnadrive import dnadrive
inp = 'input.test'
outp = 'output.test'
well = 'output.well'

tiprack = containers.load(
    'tiprack-200ul',  # container type
    'A1',             # slot
    'tiprack'         # user-defined name
)

plate = containers.load('96-flat', 'B1', 'plate')

p200 = instruments.Pipette(
    axis="b",
    max_volume=200
)

if __name__ == '__main__':
    gene = dnadrive.encode_file(inp,outp)
    outp = dnadrive.generate_well_file(outp,well)
    p200.pick_up_tip(tiprack[0])
    with open(outp,'r') as well:
        well_data = (well.read()).split('\n')[1]
        for tip in well_data.split(','):
            print('drop tip in well',tip)
            p200.aspirate(plate[tip])
    p200.return_tip()
    robot.simulate()