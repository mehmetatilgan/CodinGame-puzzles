import java.util.*;

class Player {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            List<Integer> closeOne = new ArrayList<>();
            List<int[]> humans = new ArrayList<>();
            List<Integer> humansX = new ArrayList<>();
            List<Integer> humansY = new ArrayList<>();

            int x = scanner.nextInt();
            int y = scanner.nextInt();
            int human_count = scanner.nextInt();

            for (int i = 0; i < human_count; i++) {
                int human_id = scanner.nextInt();
                int human_x = scanner.nextInt();
                int human_y = scanner.nextInt();
                humans.add(new int[]{human_id, human_x, human_y});
                humansX.add(human_x);
                humansY.add(human_y);
                closeOne.add((int) Math.sqrt(Math.pow(x - human_x, 2) + Math.pow(y - human_y, 2)));
            }

            int zombie_count = scanner.nextInt();
            for (int i = 0; i < zombie_count; i++) {
                int zombie_id = scanner.nextInt();
                int zombie_x = scanner.nextInt();
                int zombie_y = scanner.nextInt();
                int zombie_xnext = scanner.nextInt();
                int zombie_ynext = scanner.nextInt();

                for (int j = 0; j < humansX.size(); j++) {
                    int human_x = humansX.get(j);
                    int human_y = humansY.get(j);

                    if ((Math.sqrt(Math.pow(x - human_x, 2) + Math.pow(y - human_y, 2)) / 5)
                            - Math.sqrt(Math.pow(zombie_x - human_x, 2) + Math.pow(zombie_y - human_y, 2)) < 50000) {
                        closeOne.set(j, 999999);
                        humansX.remove(j);
                        humansY.remove(j);
                        break;
                    }
                }
            }

            int minIndex = closeOne.indexOf(getMinValue(closeOne));
            System.out.println(humans.get(minIndex)[1] + " " + humans.get(minIndex)[2] + " " + closeOne);
        }
    }

    private static int getMinValue(List<Integer> list) {
        int minValue = Integer.MAX_VALUE;
        for (int value : list) {
            if (value < minValue) {
                minValue = value;
            }
        }
        return minValue;
    }
}