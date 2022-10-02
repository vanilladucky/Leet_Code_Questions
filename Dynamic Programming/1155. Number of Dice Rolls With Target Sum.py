class Solution:
	def numRollsToTarget(self, n: int, k: int, target: int) -> int:

		self.memo = {}

		def solve(target,dices):

			if((target,dices) in self.memo):
				return self.memo[(target,dices)]

			if(target == 0 and dices == 0):
				return 1

			if(target == 0):
				return 0

			if(dices < 1):
				return 0

			ans = 0
			for i in range(1,k+1):
				if(target >= i): # For faster execution, not really necessary to the whole algorithm
					ans += solve(target-i,dices-1)

			self.memo[(target,dices)] = ans
			return ans

		return solve(target,n) % (7 + 10**9)
