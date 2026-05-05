---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/promql-for-native-histograms/
youtube_url: https://www.youtube.com/watch?v=fikCqhlUOmQ
youtube_search_url: https://www.youtube.com/results?search_query=PromQL+for+Native+Histograms+PromCon+2022
video_match_score: 0.908
status: video-found
---

# PromQL for Native Histograms

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/promql-for-native-histograms/
- YouTube: https://www.youtube.com/watch?v=fikCqhlUOmQ

## Resumo

Speaker(s): Björn Rabenstein So far, every sample value in a Prometheus time series has been a simple floating point value. The new Native Histograms (formerly known as Sparse Histograms) break with that tradition. The value of a Histogram sample is a fully fledged histogram, with a dynamic number of buckets and the usual count and sum of observations all included.

## Abstract oficial

Speaker(s): Björn Rabenstein

So far, every sample value in a Prometheus time series has been a simple floating point value. The new Native Histograms (formerly known as Sparse Histograms) break with that tradition. The value of a Histogram sample is a fully fledged histogram, with a dynamic number of buckets and the usual count and sum of observations all included. Dealing with this kind of “structured” samples requires fundamental changes to PromQL. Beorn will show you how those changes look like and how to use them in practice to benefit from the power of Native Histograms. This includes aggregation of Histograms, accurate estimation of quantiles, displaying Histograms in text form or as heat maps, and more. Finally, the changes of PromQL required for Native Histograms also allow us to get a glimpse of a possible future PromQL with first class support of typed and structured samples.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/promql-for-native-histograms/
- YouTube: https://www.youtube.com/watch?v=fikCqhlUOmQ
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fikCqhlUOmQ
- YouTube title: PromCon EU 2022: PromQL for Native Histograms
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/promql-for-native-histograms/fikCqhlUOmQ.txt
- Transcript chars: 29598
- Keywords: histogram, histograms, vector, prometheus, question, ganesh, already, counter, bucket, native, future, series, resolution, function, essentially, underscore, prompt, actually

### Resumo baseado na transcript

[Music] foreign [Music] I thank you [Applause] I have done one thing or two for Prometheus over the last 10 years or something and I would like to talk about prom girl for Native histograms thank you for the first question I could sense that this is exactly what you need now um this talk is only here for the people who are watching this in the future and the recording um if you watch this as a recording please watch Ganesh talk first because it sets the stage for

### Excerpt da transcript

[Music] foreign [Music] I thank you [Applause] I have done one thing or two for Prometheus over the last 10 years or something and I would like to talk about prom girl for Native histograms thank you for the first question I could sense that this is exactly what you need now um this talk is only here for the people who are watching this in the future and the recording um if you watch this as a recording please watch Ganesh talk first because it sets the stage for this talk if you're here in the room you have just seen Ganesh talk um but there's another talk of garnish from kubecon in Valencia earlier this year which is very similar to kind of Ganesh talk from today and my talk combined it's just like approaching things from first principles while this talk is fairly Hands-On so it might still make sense to watch also this talk to see kind of the other perspective and if you are really into Prometheus histograms I've given tons of talks about this and these are the three most important ones which I like to call the original trilogy and like with popular movie Frenchies it also has prequels and sequels this is the recommended viewing order but you can see this one has been produced after the second one but yeah by the way the first talk also answers a bit of this question what are the problems with the text format it gives you a lot of historical perspective and also a lot of background what was our thinking process why did we decide to do this why did it take so long like this is from like the the second talk there is kind of the centerpiece and it was given here in Munich at the last in-person prompion and did three years ago and even back then we were already talking about the past and history so this has a lot of history um so uh has a warning Ganesh said this already but since you might just watch this on the recording um this is all very experimental you need a feature flag to activate native histograms on Prometheus um don't try this in production unless you really know what you're doing because it might break in weird ways also this feature flag is only getting ingestion so if once the poor native histograms aren't your tscb they won't go away anymore even if you remove the feature flag um so yeah don't do this to your precious production tsv data [Music] um prompt girl a bit of background prompt ql is if you want a statically strongly typed language just that the types are weird and the types are instant vectors and range vectors you probably have n
