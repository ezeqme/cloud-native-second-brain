---
type: session
event: KubeCon Europe 2026 Amsterdam - Observability Day
year: 2026
kind: lightning-talk
room: "Forum (Ground Floor)"
sched_url: https://colocatedeventseu2026.sched.com/event/2DY1n/cllightning-talk-the-meta-trick-connecting-page-load-to-backend-traces-wolfgang-therrien-honeycomb
youtube_url: "https://www.youtube.com/watch?v=tucP7bhlPYU"
youtube_id: "tucP7bhlPYU"
match_score: 1.025
speakers: ["Wolfgang Therrien", "Honeycomb"]
topics: ["Metrics", "Tracing", "Logging", "SLOs", "AI Observability", "Security"]
status: "transcript-downloaded"
playlist: "Observability Day 2026 - Europe"
playlist_id: "PLj6h78yzYM2OXd3i-CyZH4A1QMxLTsKEJ"
playlist_index: 3
keywords: ["trace", "context", "spans", "traces", "span", "tracing", "telemetry", "log", "metrics", "parent", "redaction", "front-end", "little", "recommendations", "backend", "browser", "template", "observability", "honeycomb", "request", "usable", "connecting", "online", "situation"]
transcript_file: "_sources/transcripts/youtube-playlists/observability-day-2026-europe/lightning-talk-the-meta-trick-connecting-page-load-to-backend-traces/tucP7bhlPYU.txt"
---

# ⚡Lightning Talk: The Meta Trick: Connecting Page Load To Backend Traces - Wolfgang Therrien, Honeycomb

## Metadata

- Schedule: https://colocatedeventseu2026.sched.com/event/2DY1n/cllightning-talk-the-meta-trick-connecting-page-load-to-backend-traces-wolfgang-therrien-honeycomb
- YouTube: https://www.youtube.com/watch?v=tucP7bhlPYU
- Room: Forum (Ground Floor)
- Speakers: Wolfgang Therrien, Honeycomb
- Topics: [[Metrics]], [[Tracing]], [[Logging]], [[SLOs]], [[AI Observability]], [[Security]]

## Transcript

Hey folks, uh my name is Wolf Gang Theion. My pronouns are he and him. And don't worry, these slides are going to be online. Thank you for spending the next 10 minutes with me. I'm going to tell you a little bit about myself, view a common front-end situation, and then highlight a tool to help with that situation, and share some pointers for further reading. Currently, I'm the tech lead for Agentic Observability at Honeycomb. But before that, I spent a lot of my career thinking about and specializing in web and front-end technologies. Early on, I was mostly putting buttons on web pages, building out visualizations, and then trying to figure out why those web pages were slow. So, naturally, my focus shifted from building web apps to web performance and front-end observability. I've led web performance efforts at companies like HubSpot until and until my recent shift in focus, I was tech lead for Honeycomb's front-end observability team and also in charge of the Honeycomb web SDK efforts.

And it's a hard problem front end. The data is messy. The users are unpredictable. And we're sending our code into the wild and uncaring arms of the browser. I'm here to highlight a way to connect page loads and backend traces to help answer that quintessential front-end question, what's making my page slow? So, let's set the scene. You have a little online shop uh with a product page, some customized recommendations, a user hits a URL, your service HTTP handler makes a synchronous request that interrogates some feature flagged service because maybe you're doing a little AE testing. Uh also you query a database to get some information about that user, maybe that user's current cart so that in the end you can generate a personalized template for that user that gets served up to the browser. That's phase one. Then we have phase two. The browser receives the HTML, fetches some assets, some JavaScript, some stylesheets, some images, etc.

Processes the assets and then finally renders some web app content. The page is loaded but not usable. Then we have phase three might overlap with phase two. The browser fetches more data, maybe some product recommendations, processes the response and rerenders. This is the arc from the user hitting the URL to being loaded to usable. One, two, three distinct units of work, front end and back end. You generate the template, you render the page, and you load the recommendations. And you've already instrumented your code. So, good job. You have three really rich traces. You can see in your template generation, maybe your feature flag provider is a little flaky. You have some retries or failures in there. You can diagnose that. You have document load where you can see if there are slowdowns in your asset fetching or performance. Maybe you're even reporting some core web vital spans in there. And you have your follow on data loading for recommendations where you can see how long it takes to retrieve that data, parse that JSON, and render those recommendations.

And you're using endto-end tracing there. So, good job. A lot of really rich information, but all three phases are separate. You have your backend trace that details how the HTML is generated, your front-end trace that starts when the browser begins loading and ends when that document finishes, and end to end tracing for hitting the recommendations API, but it's floating over there on its own. Three traces with no clear relationship between them. So when that user report comes in and it says the product page is slow, what happens next? You look at the front end trace and your endto-end traces and maybe those look reasonable. And you look at the backend trace, but maybe it's hard to find the right one. Eventually, maybe you spot that slow database query. The problem is that you had to correlate these traces by hand. Maybe you're matching timestamps. Maybe you're looking at user IDs. You can spend a lot of time investigating here.

Or worse, you never look at the back end. You spent a bunch of time optimizing the front-end rendering when the real fix was tweaking that database call. It's not ideal, but maybe we can do a little bit better. So, let me highlight a tool that you can put in your pocket and to hopefully uh help you with this situation. And you're probably already familiar with it. It's been around for a while. It's trace parent. It's defined by W3C. Read up on it, w3c.org. Trace parent describes the position of the incoming request in its trace graph in a portable fixed length format. Takes your trace ID and your span ID. And we usually send this along for uh in our HTTP header between your various services. This is how we propagate trace ID and end to end traces. A lot of the time this is the info we need. So how do we use it to help with our scenario? We need to find a way to store and access that context later on for those traces.

We won't have easy access to that information when we need it. So we've got three steps. Step one, we take that trace parent and we embed it in the HTML page. So this is an example in a Go template. It's obviously a lot of redaction here. Um but we construct construct that trace parent using the trace ID and the parent ID from the context where we handled the initial request and just set that as the content value in our meta tag in the template. Easy. Step two, we write a little TypeScript code. If you're using TypeScript in the client and that reads the context from the HTML page in the meta tag, you probably have some code that looks very much like this. And we use the propagation API to construct that remote context. Here we're falling back to root context just in case it's not set for some reason. And step three, when you're emitting your page load telemetry, you set that context for those spans.

So here we're using context.withid with the context API as an example. But this remote context here could be a good parent for your document load, your core web vital spans, and any other data loading that you expect to finish in a reasonable amount of time. Anything that you consider to be part of that first usable experience for your app. Exactly how you do this is going to depend on your templating libraries, your backend languages, and how you're instrumenting your client, but the technique will be the same. During HTML generation, your service already inside that active span, the one handling the request. You embed that context into your meta tag. And then in your client, your TypeScript reads that meta tag on page load, builds that context, and then when you emit your page load telemetry, you can set that parent context. It's not too hard, but it's pretty powerful. So that's the how. But what does that mean for our telemetry shape?

Instead of having those three separate traces, it looks more like this. a single page load that goes from hitting the URL to loaded to usable. You've connected these three disparate traces into a single trace that shows a more complete picture of your initial page load. This will help you find the action actionable trace quickly. And now that you've gone from those three disparate traces to a really informative single trace, you might be really really tempted to parent everything under that context. And as tempting as that might be, don't do that. That's not how traces are intended to be used. So what do we do with the rest of the telemetry? Because you'll likely have other things happening on that page. Uh maybe you have some infinite scrolling, some polling or some websocket activity that your app is responding to or hopefully a checkout if you're an e-commerce site. But a parent child relationship isn't always that correct model.

So there are other mechanisms to connect those follow on telemetry signals uh whether those are spans or log events or metrics. So I'm not going to go into those details here. We'll save those tricks for another time. But I do encourage you to read up on the data models uh and SDK APIs to see if using span links for spans trace context fields for your log events or exemplars for metrics can help you create more connected telemetry for your applications to give you that more complete picture. The metatag is just one trick uh and one tool for connecting your telemetry. And the more complete and the more connected your telemetry is, the easier it will be for you to use that data to understand your system. So go and try it out. Uh thank you so much for your time and attention today. Again, these slides are online. Give it a try. Let me know if it works. Uh come and find me if you have questions about connecting telemetry shapes or how to get involved with open telemetry.

I'll be around this week. Um, and also on the CNCF Slack. Um, if you want to learn more about Honeycomb, you can find us at booth 985 and check out our other talks. Thank you so much and happy observability day.


## Notes

- Raw note. Promote durable insights to topic notes under `03-Topics/`.

## Related keywords

[[trace]] [[context]] [[spans]] [[traces]] [[span]] [[tracing]] [[telemetry]] [[log]] [[metrics]] [[parent]] [[redaction]] [[front-end]]
