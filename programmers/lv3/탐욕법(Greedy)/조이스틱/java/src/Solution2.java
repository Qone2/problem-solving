import java.util.ArrayList;

public class Solution2 {
    public static int solution(String name) {
        int count = 0;
        for (char n : name.toCharArray()) {
            if (n <= 78) {
                count += n - 65;
            } else {
                count += 90 - n + 1;
            }
        }

        ArrayList<Integer> nameArray = new ArrayList<>();
        nameArray.add(0);
        for (int i = 1; i < name.length(); i++) {
            if (name.charAt(i) != 'A') {
                nameArray.add(1);
            } else {
                nameArray.add(0);
            }
        }

        int index = 0;
        while (true) {
            if (nameArray.contains(1) == false) {
                break;
            }

            int move = 0;
            while (true) {
                move++;
                if (nameArray.get((index + move) % nameArray.size()) == 1) {
                    count += move;
                    index = (index + move) % nameArray.size();
                    break;
                } else if (nameArray.get((index - move + nameArray.size()) % nameArray.size()) == 1) {
                    count += move;
                    index = (index - move + nameArray.size()) % nameArray.size();
                    break;
                }
            }
            nameArray.set(index, 0);
        }

        return count;
    }

    public static void main(String[] args) {
        System.out.println(solution("ABAAAAAAAAABB")); //         7
        System.out.println(solution("ABABAAAAAAABA")); //        10
        System.out.println(solution("BBAAABAAAAAAAAAAAABA")); //  9
    }
}
