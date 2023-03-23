# 1472. Design Browser History

# Array Approach

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current + 1] + [url]
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]
    
    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


# Stack Approach

class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = []
        self.future = []
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history) > 1:
            self.future.append(self.history[-1])
            self.history.pop()
            steps -= 1
        return self.history[-1]
    
    def forward(self, steps: int) -> str:
        while steps > 0 and self.future:
            self.history.append(self.future[-1])
            self.future.pop()
            steps -= 1
        return self.history[-1]


browserHistory = BrowserHistory("leetcode.com")
print(browserHistory.visit("google.com"))       
print(browserHistory.visit("facebook.com"))     
print(browserHistory.visit("youtube.com"))      
print(browserHistory.back(1))                   
print(browserHistory.back(1))                   
print(browserHistory.forward(1))                
print(browserHistory.visit("linkedin.com"))     
print(browserHistory.forward(2))                
print(browserHistory.back(2))                   
print(browserHistory.back(7))                 
