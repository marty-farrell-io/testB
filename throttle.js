class TokenBucket {
    constructor(maxTokens, refillRate) {
        this.maxTokens = maxTokens;
        this.refillRate = refillRate; // tokens per second
        this.tokens = maxTokens;
        this.lastRefillTime = Date.now();
    }

    async consume() {
        await this.refill();
        if (this.tokens === 0) {
            console.log("Throttling")
            await new Promise(resolve => setTimeout(resolve, 1000)); // Wait 1 second
            await this.consume();
        } else {
            this.tokens--;
        }
    }

    refill() {
        const now = Date.now();
        const timeSinceLastRefill = now - this.lastRefillTime;
        const tokensToAdd = Math.floor(timeSinceLastRefill * this.refillRate / 1000);
        this.tokens = Math.min(this.tokens + tokensToAdd, this.maxTokens);
        this.lastRefillTime = now;
    }
}

// Example usage
const bucket = new TokenBucket(10, 1); // 10 tokens, 1 token/second
async function makeRequest() {

    await bucket.consume();
    // Your API request logic here
    fetch("https://www.google.com")
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.status;
      })
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
}


for (let i = 0; i < 20; i++) {
    makeRequest();
}