## Week 7 — Issue selection

**Issue link:** https://github.com/ascherj/pathreview/issues/86

**Issue title:** Add an API rate limiting header (`X-RateLimit-Remaining`) to responses

**Tier:** [ ] Tier 1  [ X ] Tier 2  [ ] Tier 3

**Problem summary:**

Currently, there is no way to for API clients to know how many requests they have remaining before requests are blocked with a 429 error. This feature adds `X-RateLimit-Limit` and `X-RateLimit-Remaining` headers to each request so that users can track available rate limit, and requests remaining per session. This improvement affects `api/middleware` and `safety/rate_limiter.py`, and a successful implementation adds middleware that adds the headers to each request. The implementation may use similar JWT decode logic as in `middleware/auth.py` for use as the identifier arg for `safety/rate_limiter.py` and may use similar attachment logic to that in `request_id.py` to attach the rate limiter headers to the request. The implementation will also need to handle returning the 429 response, as currently there is no logic for raising and returning an appropriate response. After implementation, each request will include the new headers. 


**Checklist reasoning:**

My last two semesters of school have involved creating web apps, so I am familiar with HTTP request/response headers. I took additional time to understand the role of the middleware sections for PathReview, so while rate limiters are a new feature for me, I am familiar with the pieces involved. It is a Tier 2 issue, but I have made a few contributions to a small OSS project in the last two months, so I am no longer overwhelmed by navigating a large codebase. My contributions have been more scoped to tier 1 issues, so this issue selection represents a manageable step up from my past contributions. Given the time I have available for the remaining course term, I am confident I will be able to complete this, and potentially another issue, before the course term ends. 

**Branch name:** feat/86-ratelimit-header

**Setup confirmation:** [ X ] App runs locally at localhost:5173

**Cohort ledger:** [ X ] Issue added to cohort ledger