---
type: session
event: "PromCon EU 2025"
year: 2025
kind: session
youtube_url: "https://www.youtube.com/watch?v=5lRty1G1wNM"
youtube_id: "5lRty1G1wNM"
playlist: "PromCon EU 2025"
playlist_id: "PLj6h78yzYM2P534LgwCVm3GQdxLcSt7We"
playlist_index: 30
speakers: ["Bartek Protka"]
topics: ["Collectors", "Metrics", "SLOs", "AI Observability"]
keywords: ["metric", "metrics", "collector", "actually", "collection", "memory", "killing", "important", "server", "decision", "series", "dilemma", "incoming", "cardality", "solution", "second", "scrape", "experiment", "ethical", "questions", "situation", "reduce", "difficult", "promeuse"]
transcript_file: "_sources/transcripts/youtube-playlists/promcon-eu-2025/lightning-talk-scrape-trolley-dilemma/5lRty1G1wNM.txt"
transcript_chars: 5393
status: "transcript-downloaded"
match_score: 1.08
---

# Lightning Talk: Scrape Trolley Dilemma - Bartek Protka

## Metadata

- YouTube: https://www.youtube.com/watch?v=5lRty1G1wNM
- Playlist: PromCon EU 2025
- Speakers: Bartek Protka
- Topics: [[Collectors]], [[Metrics]], [[SLOs]], [[AI Observability]]

## Transcript

Yeah, I want to talk about trumps and how they can help us to really show the problem um we are facing in yeah in collection. So hello everyone again. Um let's talk about collection resiliency. Um yeah we have some kind of feature which would be nice to have but it's kind of blocked on some um yeah some kind of dilemma. Um and it's really similar or it's you maybe you recognize this you know uh tran trolly dilemma and that's how it's called officially. It's kind of like a cool experiment thought experiment about ethical problems ethical questions. Um so what would happen if you would be in a in a situation where traum is incoming and you know some people might be hurt. Um and you have sort of control to reduce that um you know that that that kind of situation to maybe uh you know le that less people are hurt but still they are hurt and it's really like very odd very difficult to find figure out who are you then responsible should you do this or not and it's not very easy to answer and I think we sort of have this problem right now with collection resilency take it with a grain of salt of course we are not killing people hopefully we are killing metrics but or servers But it's uh yeah maybe metric is so important that it actually causes planes to you know go down then it's kind of important.

So how to really map this out? If you imagine the traum is incoming data it's for example when we are scraping the data and you are and the promeuse and the code we are developing and configuration we are putting into propuse server to decide things is this guy on the liver. Um and you are you know that promeuse you are this primeuse process and you know you are close to memory limit. You sort of have two choices here. If you see a very expensive data incoming and you are super close to memory limit, you see data like this which have like very cardality, very high cardality like um dimension in it, you know things will go wrong. So traum is going definitely in the direction of crash loop, right? Your server will be down, your collection will be down, your likely quering will be down as well. Um so you have a choice. You can kind of maybe stop this scrape job. you could stop um maybe you can ignore this metric this one metric maybe will be better than killing the whole server and it's actually not only promeus it's also open telemetry collector any collector decision when we are pulling metrics this is like difficult this uh you know decision to make because it's not easy to really tell what metric to kill um who should make this decision because there is no good solution uh what happens when you kill those series you don't know if it's important or not and I want to show what kind of auto is doing and auto of course um have this it actually kills random let's say pushes on the push side it's a little bit more easier because when you push you kind of expect uh or you are receiving pushes you are kind of expecting that people kind of retry so sort of maybe you can slow down for a second and clients can retry but you know eventually they will kind of collapse because um the client cannot buffer unlimitedly they they it has to kind of collapse so essentially um this push receiver memory limit is kind of pushing the problem somewhere else right okay it's not my problem actually yeah do you do it I just cannot commit to this take find another collector so that's kind of like a benefit and downside of the push the so they don't need to make this decision right they're not killing anybody it's like client kind of like have to deal some with stuff but we have a problem and essentially um I just want to clarify this problem and kind of make any progress towards solution and we need to really your feedback as the user what would you like to do right we have bunch of things we could do we could kind of maybe have some flashing early like garbage collection kind of early compaction to just you know like reduce the memory u for some sacrifice of like I don't know like a block size in the storage maybe we could actually slow down scrapes so kind of like maybe okay you you want every second metric every 10-second metric interval maybe make it one minute for for a bit I mean your monitoring should be fine right but And actually samples is not the main memory usage factor or contributor actually it's new series so cardality.

So maybe you don't add more series or maybe for certain series. But then there's so many questions and all of those there's no perfect solution. But my point is like let's iterate. Let's have something dump naive and iterate over it. Let's make sure we get your your feedback if it's useful. If you know what to kill. In my opinion, we should have it because I think we should kind of kill one metric than the whole server and I think we should have something in my opinion behind you know optional kind of flag and I think in the future we are talking about telemetry health. So metric every metric would be you know we are talking about schema it would have additional information about criticality of this metric. Hey, these pieces of metrics are critical because it's autoscaling, because it is, you know, super important alerting metric. Don't kill it. Right. But there are some experimental metrics. Yeah, you can kill like my collection will survive.

So, you could do it by basel. Yeah. Fantastic. Thank you.


## Related keywords

[[metric]] [[metrics]] [[collector]] [[actually]] [[collection]] [[memory]] [[killing]] [[important]] [[server]] [[decision]] [[series]] [[dilemma]]

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
