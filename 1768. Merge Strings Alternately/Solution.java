class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder out = new StringBuilder();
        int p1 = 0;
        int p2 = 0;

        while (p1 < word1.length() || p2 < word2.length()) {
            if (p1 < word1.length()) {
                out.append(word1.charAt(p1));
                p1++;
            }
            if (p2 < word2.length()) {
                out.append(word2.charAt(p2));
                p2++;
            }
        }

        return out.toString();
    }

    public static void main(String[] args) {
        String word1 = "ab";
        String word2 = "pqrs";
        Solution solution = new Solution();
        String merged = solution.mergeAlternately(word1, word2);
        System.out.println(merged);
    }
}