public class Main {
    
    public static void getIndices(int[] arr) {
        int maxi = arr[0], sum = 0;
        int start = 0, temp = 0, end = 0;
        
        for(int i = 0; i < arr.length; i++) {
            sum += arr[i];
            
            if (sum > maxi) {
                maxi = sum;
                start = temp;
                end = i;// Update the start index when a new maximum is found
            }
            
            if (sum < 0) {
                sum = 0;
                temp = i + 1;  // Move the temp start index to the next position
            }
        }
        
        System.out.println("Max sum: " + maxi + ", Start index: " + start
        + ", End index: " + end);
    }

    public static void main(String[] args) {
        getIndices(new int[] {1, -2, -3, 4, 4, -2});
    }
}
