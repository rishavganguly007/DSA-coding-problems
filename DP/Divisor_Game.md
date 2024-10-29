DivisorGaame
```python
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
```
![image](https://github.com/user-attachments/assets/19de9e01-94b5-4a01-be9d-d381eff2be03)


Optimal pplay is removing the chances of players to play a alternative move, ie -> find a direct path for the current player (no branches)

aka, if the n is even Alice will have the direct path highlighted in yelow, and vice versa
