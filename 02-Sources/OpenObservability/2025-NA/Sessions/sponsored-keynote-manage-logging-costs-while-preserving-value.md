---
type: session
event: "Open Observability Summit + Otel Community Day NA 2025"
year: 2025
kind: session
youtube_url: https://www.youtube.com/watch?v=Z4umnlRdLtA
youtube_id: Z4umnlRdLtA
playlist: "Open Observability Summit + Otel Community Day NA 2025"
playlist_id: PLj6h78yzYM2NFT2PGItX2idBf7v8fHcy7
playlist_index: 3
speakers: ["Alok Bhide", "Chronosphere"]
topics: ["Collectors", "Metrics", "Logging", "Cost Optimization", "AI Observability"]
keywords: ["logs", "logging", "log", "pipeline", "error", "metric", "fluent", "product", "expensive", "engineers", "customers", "launched", "source", "specifically", "solution", "generated", "change", "analyze", "improvements", "manage", "preserving", "chronosphere", "simple", "telemetry"]
transcript_file: _sources/transcripts/youtube-playlists/open-observability-summit-otel-community-day-na-2025/sponsored-keynote-manage-logging-costs-while-preserving-value/Z4umnlRdLtA.txt
transcript_chars: 5407
status: transcript-downloaded
---

# Sponsored Keynote: Manage Logging Costs While Preserving Value - Alok Bhide, Chronosphere

## Metadata

- YouTube: https://www.youtube.com/watch?v=Z4umnlRdLtA
- Playlist: Open Observability Summit + Otel Community Day NA 2025
- Speakers: Alok Bhide, Chronosphere
- Topics: [[Collectors]], [[Metrics]], [[Logging]], [[Cost Optimization]], [[AI Observability]]

## Transcript

I'm going to talk to you guys about uh I'm I'm Aloque. I'm the head of product innovation at Chronosphere. Um I'm going to talk to you about what we've launched as of this or announced as of Tuesday this week. A capability that helps you manage logging costs while preserving value. But I'm also going to take it back to how we contributed to the open source community specifically Fluent Bit as we did this. So why are we still talking about logs? It's quite simple. Logs are expensive. uh all telemetry is expensive but logs have a dubious quality where they're not they are very obviously not all equal and but the problem I've that I've seen um admins or tools owners face throughout the entire you know life life cycle of log logging tools is that they don't know how to tell which logs are valuable and which ones are not and this comes up time and time again every time I speak with any customer this is their primary pain point not the engineers not the execs but those who are responsible for the tools they're caught in a rock in a hard place.

So how do some product vendors how do certain solutions how do certain customers deal with this? Often cheaper storage S3 backing uh on any other object store is usually part of the solution and this is a good solution. I'm not I'm not saying anything bad about these solutions. This is a viable solution and needs to be there and available. uh but you're often making some sort of trade-off in often performance when you're taking take making this choice. Moreover, you're kicking the can down the road. Even if it's cheap, at some point it's going to become expensive again. So that's what we've seen. Things just get expensive because telemetry just grows and logs grow with it. So the way we look at it is we can't really if you look at the source of logs, which is where logs are generated often, you name it. We're not going to go into how logs are generated, but they're easy to generate. It's very difficult to retrain people to change standards in a company and do that consistently as a vendor especially or any product cannot necessarily change how logs are generated or you know change the behavior of folks.

But what we can do is help these admins or tools owners on the side of the pipeline and the logging management tool or log management tool. We look at this as a way where we can help these folks analyze the value of these logs, really deeply analyze the value of these logs, recommend those changes or transformations or optimizations right there and also provide the tools to act on those transformations, reuse those logs in one way or another. But specifically, so this is a screenshot from what we just launched. Um, this is not the entire logging product. This is specifically the logs usage analysis screen as we call it. And this delivers that value which is how do you analyze the value of a log and we do a comprehensive analysis of the logs as they are used by the engineers and we determine a utility score and then we tell you know the customers generally look at that and say tell me the lowest value highest volume logs that's the easiest thing to do and this is an example of how that looks extremely low value log in this example um low utility score because we know how those logs are used by those engineers in this case not at all.

Now, this is a very simple example where the recommendation at the top says just drop those logs. But most often it's not these there's lots of logs that fall into this category. But there are many logs that fall into a mixed category. They're used on dashboards or but not in logs searches or they're highly similar and they don't add more value by having 10 more of those types of error logs or things like that. So we have ways and recommendations where we help maintain that value for customers. So we can make more sophisticated recommendations like why don't you go ahead and uh convert those logs to a metric count the logs and then drop those logs. That means you still retain some of the value of the logs that the engineers need which is the error counts but you don't necessarily have to keep all the volume and this is what has been exciting for our customers. As I said um I was going to bring it back to the open source uh contributions we made.

We made very specific on the ACT portion which I didn't really talk about too much today. uh not enough time but the ability to actually transform the data on the pipeline. We made uh improvements to fluent bit in order to make that a lot easier. So we've added the ability to have a conditional processing rule. What that means is for any processing rule or a processor in fluent bit you can now apply a condition to it which means only those logs that match that rule uh are processed by that rule. Could be dropping could be transforming that particular log in any one way or another. What that means is fast forward what's the benefit? You now need fewer fluent bit instances uh to run in order to have a effective pipeline. In the past you'd have to have multiple fluent bit instances fired up to be able to do this. It's a lot easier and obviously we made tons of resiliency improvements. I forgot to mention this is available in fluent bit version 4 which is just launched recently and we made tons of resiliency improvements in the process as well.

And with that, thank you very much and I'll hand it back to

## Related keywords

[[logs]] [[logging]] [[log]] [[pipeline]] [[error]] [[metric]] [[fluent]] [[product]] [[expensive]] [[engineers]] [[customers]] [[launched]]

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
