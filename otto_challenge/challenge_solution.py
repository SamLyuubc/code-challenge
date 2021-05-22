import sys

def main():
   # Using readlines()
   input_file = open('sample_input_large.txt', 'r')
   output_file = open('sam_ouput_file', 'w')
   lines = input_file.readlines()
   path_string_list = [line.split() for line in lines]
   line_num = 0
   for entry in path_string_list:
      if (len(entry) == 1):
         path_len = int(entry[0])
         # skip if there is no way points included
         if path_len == 0:
            continue
         # Construct a full list of path points
         path_list=[]
         path_list.append(['0', '0', '0'])
         path_list += path_string_list[line_num+ 1: line_num + path_len + 1]
         path_list.append(['100', '100', '0'])
         # Calculate the least effort to finish the path
         result = round(calculateMinimumCost(path_list), 3)
         output_file.write(str(result))
         output_file.write("\n")
      line_num += 1

def calculateMinimumCost(path_list):
   accumulated_penalty_list = []
   # minimum_effort to get to staring point is 0
   minimum_effort_list = [sys.maxsize] * (len(path_list))
   minimum_effort_list[0] = 0
   accumulated_penalty = 0
   way_point_index = 0

   for way_point in path_list:
      # Convert string to int
      way_point = list(map(int, way_point))
      accumulated_penalty += way_point[2]
      accumulated_penalty_list.append(accumulated_penalty)
      if (way_point_index > 0):
         point_index = 0

         for point in path_list[0:way_point_index]:
           # time needed to travel from starting point to the target point
           travel_time =0.5 * ((way_point[0] - int(point[0]))**2 + (way_point[1] - int(point[1]))**2)**0.5
           # total_effort is the sum of travel_time, penalty for skipping the points in between and 10 second operation time on the spot
           total_effort = travel_time + accumulated_penalty_list[way_point_index] - way_point[2] - accumulated_penalty_list[point_index] + 10
           # Add the minimum_effort of the starting point
           minimum_effort = total_effort + minimum_effort_list[point_index]
           # Update the minimum_effort for the target point
           if (minimum_effort < minimum_effort_list[way_point_index]):
              minimum_effort_list[way_point_index] = minimum_effort

           point_index += 1
      way_point_index += 1
   return minimum_effort_list[-1]

if __name__ == "__main__":
   main()
