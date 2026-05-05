---
type: session
event: "PromCon EU 2025"
year: 2025
kind: session
youtube_url: "https://www.youtube.com/watch?v=E2iFLFYHm6M"
youtube_id: "E2iFLFYHm6M"
playlist: "PromCon EU 2025"
playlist_id: "PLj6h78yzYM2P534LgwCVm3GQdxLcSt7We"
playlist_index: 28
speakers: ["Igor de Sousa"]
topics: ["AI Observability"]
keywords: ["information", "trying", "monitoring", "thinking", "observability", "device", "experiment", "figure", "context", "systems", "observe", "engine", "cannot", "mechanic", "monitor", "better", "thought", "perspective", "sometimes", "access", "actually", "getting", "happens", "identify"]
transcript_file: "_sources/transcripts/youtube-playlists/promcon-eu-2025/lightning-talk-observabilitywithout-monitoring/E2iFLFYHm6M.txt"
transcript_chars: 5593
status: "transcript-downloaded"
match_score: 1.08
---

# Lightning Talk: ObservabilityWithout Monitoring - A Thought Experiment - Igor de Sousa

## Metadata

- YouTube: https://www.youtube.com/watch?v=E2iFLFYHm6M
- Playlist: PromCon EU 2025
- Speakers: Igor de Sousa
- Topics: [[AI Observability]]

## Transcript

Hello. After Bjorn's talk, I was thinking about the definitions of observability and monitoring. I learned a lot here and I tried to figure out since he said that uh maybe a good definition was that monitoring leads to observability. Is there a situation where maybe that doesn't apply? Let's try to experiment and see if we can find something. First, a bit context about myself. I deal mostly with bare metal hardware. All my machines run Windows. I'm in a very different context than all you guys. So uh don't I'm not talking about my work. I'm trying to draw from different experiences and try to bring a different perspective here. Uh so when I get monitoring I'm trying to diagnose systems. I'm trying to improve performance. It uh this may translate a bit and bring a different perspective maybe. Uh I also really like splitting hairs. So there's going to be some philosophy here. Uh just thoughts for us to think about what could be.

So very different context thinking about the car like uh most of you I assume don't even know what half of these fluids are. Uh but that is something that a user can observe on their system on their car if they open the hood they can get uh data from is this full or is this not full and sometimes there's monitoring on those but I would say that uh engine oil in some cars have it uh but many cars you have to go there and check otherwise you don't know until the car starts smoking or something gets wrong. Uh so maybe there's a nuance there. Uh and even to get that information can be very hard. Uh these cars here they have a frunk and a trunk and you cannot really get to the engine very easily. Some you can remove some of the covers to get some access but a mechanic would go from the bottom to actually perform maintenance on that car. So here we're starting to see a pattern where uh in cars it's actually being getting harder to monitor what's happening there.

Uh even though if you ask the manufacturer maybe there is something that they can observe. Uh here I almost forgot this is another example. If you get an electric car you can see even less like this car has a frunk and a trunk but uh the engine system is so different that it assumes that the normal user cannot get the information. They're just supposed to maybe add a bit of liquid somewhere. Uh so it's not a good solution unless you have one of these. So yes, you can get observability if you connect a device that will give you access to the monitors. Then I start asking which one's better. So here we have two systems. Uh this here is an alert that is waiting for the right time to happen. Here no one's observing this until the alert happens. But there's a physical alert that will draw everyone's attention. uh while this one here requires wires to be able to identify more points of failure. So there yes there is monitoring on this one but I would argue that the observability on this one may be better matter of opinion.

So I'm thinking about a thought experiment here. think start thinking if you don't have that device that will give you information about the car you cannot go there maybe you can't even open the hood uh just trying to see if it was a black box something that you are just trying to extract information from the system uh you have to talk to the mechanic and explain oh when I accelerate this happens and you know how good users are explaining what's going on right uh there's a lot of biases maybe they don't understand maybe they lie on purpose maybe they lie by mistake but the information doesn't get across And uh you can get some weird situations or try to figure out, but uh you can't really have all the information that you need. Imagine if you went to a mechanic, he got a bit of the oil and said, "I'm going to send it to a lab and in two weeks you have the result to see what's wrong with your car." So that wouldn't be good.

Uh there there are different ways that you have to think about certain systems. Uh even worse, like when you get to this here, uh Europeans here look at this and might say this ratings are wrong. that's too low for my car. Sometimes even uh it's hard to get the message across of what has to be changed and uh some people don't even believe when they say your car needs 91. You're going to suffer if it's not that. Uh now uh I was hiding a bit of the goal. Uh does anyone have an idea where I'm trying to get at? No. No hints. So there's a device that I believe is the equivalent of the OBD device for the topic that I'm really aiming to talk about here, the triorder or more specifically the medical triorder. Maybe in science fiction we had the system that could point and say, "Hey, this is what I've diagnosed that has to be fixed with this person." But we have very little of that. Uh most of you don't probably don't even know about uh continuous glucose monitor.

So that's something that you can monitor your body and know how food affecting glucose. Uh is that okay so maybe you can get the link afterwards more devices maybe get correlation been trying to uh figure out how we can get better information and observe our own bodies. It's very important to do that as well and we shouldn't forget about getting the uh the information that our body is telling us and we are not very good at knowing the same way that I was saying that the users can tell what's going on. We may not be good at saying what's wrong with us and identify what our body is telling us. So if anyone wants to see the presentation, leave comments there or reach me afterwards. Happy to talk about it. Thank you. >> Thank you.


## Related keywords

[[information]] [[trying]] [[monitoring]] [[thinking]] [[observability]] [[device]] [[experiment]] [[figure]] [[context]] [[systems]] [[observe]] [[engine]]

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
