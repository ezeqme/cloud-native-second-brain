---
type: session
event: "PromCon EU 2025"
year: 2025
kind: session
youtube_url: "https://www.youtube.com/watch?v=qlIddtcze7U"
youtube_id: "qlIddtcze7U"
playlist: "PromCon EU 2025"
playlist_id: "PLj6h78yzYM2P534LgwCVm3GQdxLcSt7We"
playlist_index: 32
speakers: ["Julius Rickerti"]
topics: ["Metrics", "AI Observability"]
keywords: ["metrics", "prometheus", "metric", "labels", "victoria", "instant", "trying", "exporter", "scalar", "vectors", "scalars", "julius", "worked", "location", "binary", "applies", "reason", "values", "implemented", "victory", "lightning", "rickerti", "looking", "anomaly"]
transcript_file: "_sources/transcripts/youtube-playlists/promcon-eu-2025/lightning-talk-instant-vectors-scalars/qlIddtcze7U.txt"
transcript_chars: 3259
status: "transcript-downloaded"
match_score: 1.08
---

# Lightning Talk: Instant Vectors ≠ Scalars - How it bit me - Julius Rickerti

## Metadata

- YouTube: https://www.youtube.com/watch?v=qlIddtcze7U
- Playlist: PromCon EU 2025
- Speakers: Julius Rickerti
- Topics: [[Metrics]], [[AI Observability]]

## Transcript

Hi, I'm Julius. Um, and um, yeah, I'm trying to tell you how, uh, yeah, instant vectors aren't scalars are and how that bit me. Um, I was looking at some graph and there's some anomaly down there and then I tried to zoom in and then there was no data and then I thought like what the heck, how's that possible? And uh yeah, you have to keep in mind we're using Victoria metrics for this. So it might behave differently with uh Prometheus. Um yeah, what's happening? What's the graph? Uh we're trying to assess whether uh a target is available with a blackbox exporter. And uh we're trying to um do that from different locations and only alert if uh a threshold of them agrees that things are down. Um so we don't have to wake up when things aren't in order but yeah only for some things. Um yeah and then I turned things around like I just switched um things and then it worked. And I was wondering why. Um, yeah, then it worked.

And this is kind of how the data looks. So, importantly, the exporter location counter doesn't have any labels that might become important later. Um, yeah, and there you can see the query again. Um, yeah, Victoria tries to be smart here and it does a right hand side label push down. So it uses uh the labels um that we have like for our example data we have two host names in this case A and B and uh Victoria Metrics uh recognizes that it's on the left side of the query of the binary operator and then it does a label push down. So it uh takes this thing and applies it to the count exporter location too. Um, but that doesn't work because it doesn't have any labels. Um, yeah. And if you turn it around, it works for some reason. Um, yeah. And why didn't it why did it work? Uh, unless I zoomed in. That's because there's an optimization that only applies uh if you have less than 100 um unique values. So when you zoom in, you have less values and then you don't get any data back.

Um yeah, I was using a a metric or an instant vector as a scalar. Um and yeah, that shouldn't have happened. Then I can add a scalar function and then it works. But what I should have done is add some label so I can add things later if we want to have a a parallel setup for something else. Um but now my question is why did it ever work? Um, is this something of pictoriometrics? Is it that there's a I don't know if you don't have any labels, it's supposed to match everything. What is it? >> One, two, three. Uh, yeah. Um, it was me who implemented this smart behavior. >> Yeah. Um I didn't remember actually the actual reason uh why victory metrics automatically converts um the real metric into scalar. It was implemented uh in the first days of victory metrics. So probably that's a bug which must be fixed. >> Yeah like Prometheus none of these two would ever have returned anything. Okay. So no labels matching.

>> Yeah. Good to know. Um yeah, I just took a look at the binary operators uh where it's documented, but I yeah, apparently it works as it should with Prometheus. And uh there's the issue I opened with Victoria uh late last year. Uh it's it has been handled and it's been closed because I didn't care too much about it at the time. Um yeah, if you want to get in touch with me, uh that's my GitHub. Thank you very much.


## Related keywords

[[metrics]] [[prometheus]] [[metric]] [[labels]] [[victoria]] [[instant]] [[trying]] [[exporter]] [[scalar]] [[vectors]] [[scalars]] [[julius]]

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
