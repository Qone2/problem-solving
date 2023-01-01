import java.util.ArrayList;
import java.lang.Math;

public class Solution {
    public static int solution(int n, int[] lost, int[] reserve) {
        ArrayList<Integer> lostList = new ArrayList<>();
        for (int l : lost) {
            lostList.add(l);
        }
        ArrayList<Integer> reserveList = new ArrayList<>();
        for (int r : reserve) {
            reserveList.add(r);
        }
        for (int i = reserveList.size() - 1; i >= 0; i--) {
            if (lostList.contains(reserveList.get(i))) {
                lostList.remove(reserveList.get(i));
                reserveList.remove(i);
            }
        }
        int count = n - lostList.size();
        for (int i = reserveList.size() - 1; i >= 0; i--) {
            for (int j = lostList.size() - 1; j >= 0; j--) {
                if (Math.abs(lostList.get(j) - reserveList.get(i)) == 1) {
                    count++;
                    lostList.remove(j);
                    break;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int[] lost = {2, 4};
        int[] reserve = {1, 4, 5};
        System.out.println(solution(5, lost, reserve));
    }
}
