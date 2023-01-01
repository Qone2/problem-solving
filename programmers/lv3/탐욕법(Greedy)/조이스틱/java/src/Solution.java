public class Solution {
    public static int solution(String name) {
        int count = 0;
        boolean reverse = false;
        int endPoint = name.length();
        if (name.length() == 1) {}
        else if (name.charAt(name.length() - 1) != 'A' && name.charAt(1) == 'A') {
            reverse = true;
            for (int i = 1; i < name.length(); i++) {
                if (name.charAt(i) != 'A') {
                    break;
                }
                endPoint = i;
            }
        } else {
            for (int i = name.length() - 1; i >= 0; i--) {
                if (name.charAt(i) != 'A') {
                    break;
                }
                endPoint = i;
            }
        }

        if (reverse == false) {
            for (int i = 0; i < endPoint; i++) {
                if (i == 0) {
                    count--;
                }
                count++;
                if (name.charAt(i) <= 78) {
                    count += name.charAt(i) - 65;
                } else {
                    count += 90 - name.charAt(i) + 1;
                }
            }
        } else {
            if (name.charAt(0) <= 78) {
                count += name.charAt(0) - 65;
            } else {
                count += 90 - name.charAt(0) + 1;
            }

            for (int i = name.length() - 1; i > endPoint; i--) {
                count++;
                if (name.charAt(i) <= 78) {
                    count += name.charAt(i) - 65;
                } else {
                    count += 90 - name.charAt(i) + 1;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        System.out.println(solution("ABAAAAAAAAABB"));
    }
}
