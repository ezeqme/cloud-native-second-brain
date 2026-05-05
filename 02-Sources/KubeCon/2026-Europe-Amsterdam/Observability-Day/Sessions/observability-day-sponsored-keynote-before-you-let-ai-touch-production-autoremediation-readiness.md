---
type: session
event: KubeCon Europe 2026 Amsterdam - Observability Day
year: 2026
kind: keynote
room: "Forum (Ground Floor)"
sched_url: https://colocatedeventseu2026.sched.com/event/2DdrH/observability-day-sponsored-keynote-before-you-let-ai-touch-production-autoremediation-readiness-colleen-white-chronosphere
youtube_url: https://www.youtube.com/watch?v=ziRCcF1SNko
youtube_id: ziRCcF1SNko
match_score: 0.826
speakers: ["Colleen White", "Chronosphere"]
topics: ["AI Observability"]
status: transcript-downloaded
---

# Observability Day | Sponsored Keynote - Before You Let AI Touch Production: Autoremediation Readiness - Colleen White, Chronosphere

## Metadata

- Schedule: https://colocatedeventseu2026.sched.com/event/2DdrH/observability-day-sponsored-keynote-before-you-let-ai-touch-production-autoremediation-readiness-colleen-white-chronosphere
- YouTube: https://www.youtube.com/watch?v=ziRCcF1SNko
- Room: Forum (Ground Floor)
- Speakers: Colleen White, Chronosphere
- Topics: [[AI Observability]]

## Transcript

Hello everybody. Uh my name is Colleen White. I'm with Kronosphere, a PaloAlto networks company uh as of a couple of months ago. And this feels like a really good talk to have an extension from from Sean's who just spoke because I'm going to talk a little bit about how do you get your system ready for auto remediation. Uh and just lucky me first time no notes. Uh so here we go. We'll see how it goes. Um, so the dream of observability systems have obviously always been to make it so that you know, don't just make it easy for me to find and fix problems, but ultimately in a perfect world, fix them for me so I don't even have to think about it. You can just tell me, hey, there is this issue coming up and we've solved it for you.

With AI and with some of the agentic workflows, it feels like we're closer than ever to achieving that dream. However, uh a auto remediation isn't just something that you tack on top at the end, but it's sort of the last step in a much more foundational set of uh work that you need to do to get your observability system ready. So, in the next hopefully very short four or five minutes, I'm going to just run through the sort of auto remediation readiness checklist. There's three key things to think about. First, do you have all of the data? Do you have all of the context? And do you have all of the right guardrails in place for your auto remediation? Now Sean said it really well in some ways uh from the co uh data perspective getting instrumentation and coverage has never been easier than it is today.

Um thanks to OTEL we've moved from proprietary vendor locked in systems to now uh hotel is really the TCP IP of observability. Um it's moved from a service uh you know product that you buy to a utility that you just plug into. This is good. However, I don't have to tell you guys here the scale of the data is more than it has ever been. you know, five years ago, you maybe were running a hundred VMs to run your services and now you've got a thousand pods that uh because of HPA are only up for 15 minutes. The underlying logic hasn't changed, but the volume of metadata has increased by 10fold. So, you need your AI to be able to navigate across all of that data at scale and you want it living in the same systems.

Checklist number one, do you have all of the data? Full coverage at scale. you can't, you know, automate what you can't see. But having the data isn't enough. If you just have raw data and you're asking your agents to try to navigate it, it's like having a very fast, very confused intern. They're working quick, but they're not actually making a lot of sense. There's two places to think about where you can look for context. Obviously, first from inside your observability system, you want to make sure that the data is normalized. obvious things, but if you are running 10 services and each of them have a different format for their time series, your AI is going to burn through half of its compute just trying to standardize on around the x-axis.

You also want to make sure that all of the data is linked and that all of your melts uh is accessible. LLMs are great at understanding what a metric label might mean or what the name means, but it isn't going to be able to tell you service A is dependent on an upstream service uh you know for service B and you need to be able to link those pieces. There's also a lot of instances you might want to link context from outside your observability system. For instance, when is the weather forecast an observability metric. Well, let's say that work for United Airlines in Chicago and you're in charge of the frequent flyer service uh application. Well, you know that an ice storm is coming. There's going to be an awful lot of people, thousands of requests that are hitting that service to try to change their flights.

If you have context pulled in from the weather system to be able to tell you that that ice storm is coming, you can leverage predictive autoscaling to help your system understand where you might need more capacity. So all of the context from both inside and outside your system. You've got that, you've got the data, you're ready to go. But of course, you want some guardrails in place. There's kind of a few things to think about. One of them is, is this an appropriate issue to actually use for auto remediation? You want things that are, you know, repeatable issues that uh have really standard sort of types of problems that lead to it. And of course, you want to make sure that there are clear two-way doors.

So, you know, it's very easil easy to toggle a feature flag or roll back a feature flag or clear a cache. Uh but, you know, rolling back a database migration or the changing of a schema, that's a much harder change to make. Not the kind of thing that's appropriate for auto remediation. And finally, you always want to think about how you leverage human in the loop. This is something that everybody talks about. There's kind of three things to think about here. The first that everybody talks a lot about is, you know, I want along the way to see and validate that this is a change that we're ready to auto remediate and I the human say yes. That's step one. Another thing to understand is what's the impact of actually being able to leverage auto remediation?

How much time did it save? But maybe the most important is what are the consequences if we remediated something that didn't actually need the help? Can we live with that sort of impact? Um, if you use the self-driving car analogy, it's a little bit like, yes, I drove a million safe miles, but what happens at mill uh mile a million and one? Can we live with, you know, it running into the back of a tree? So, that's it for today. Three key things to think about and leave. Do you have all the data at coverage at scale? Do you have all of the context both internal and external? And finally, do you have the right guard rails in place, right types of problems, clear two-way doors, and clear human in the loop processes?

Thanks very much. Uh, come visit us at Chronosphere's booth, both upstairs today and on the main floor tomorrow. And I hope to see you all later. Bye.

## Notes

- Raw note. Promote durable insights to topic notes under `03-Topics/`.
