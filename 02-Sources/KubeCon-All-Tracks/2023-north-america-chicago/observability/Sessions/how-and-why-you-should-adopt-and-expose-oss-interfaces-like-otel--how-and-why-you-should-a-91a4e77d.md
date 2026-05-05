---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Observability"
themes: ["Observability"]
speakers: ["Daniel Hrabovcak", "Shishi Chen", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2wI/how-and-why-you-should-adopt-and-expose-oss-interfaces-like-otel-prometheus-daniel-hrabovcak-shishi-chen-google
youtube_search_url: https://www.youtube.com/results?search_query=How+and+Why+You+Should+Adopt+and+Expose+OSS+Interfaces+Like+Otel+%26+Prometheus+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How and Why You Should Adopt and Expose OSS Interfaces Like Otel & Prometheus - Daniel Hrabovcak & Shishi Chen, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Chicago
- Speakers: Daniel Hrabovcak, Shishi Chen, Google
- Schedule: https://kccncna2023.sched.com/event/1R2wI/how-and-why-you-should-adopt-and-expose-oss-interfaces-like-otel-prometheus-daniel-hrabovcak-shishi-chen-google
- Busca YouTube: https://www.youtube.com/results?search_query=How+and+Why+You+Should+Adopt+and+Expose+OSS+Interfaces+Like+Otel+%26+Prometheus+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How and Why You Should Adopt and Expose OSS Interfaces Like Otel & Prometheus.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2wI/how-and-why-you-should-adopt-and-expose-oss-interfaces-like-otel-prometheus-daniel-hrabovcak-shishi-chen-google
- YouTube search: https://www.youtube.com/results?search_query=How+and+Why+You+Should+Adopt+and+Expose+OSS+Interfaces+Like+Otel+%26+Prometheus+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=D71fK2MFreI
- YouTube title: How and Why You Should Adopt and Expose OSS Interfaces Like Otel... - Daniel Hrabovcak & Shishi Chen
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-and-why-you-should-adopt-and-expose-oss-interfaces-like-otel-prome/D71fK2MFreI.txt
- Transcript chars: 23992
- Keywords: prometheus, monarch, google, monitoring, metrics, actually, promql, labels, already, remote, source, learned, daniel, otel, available, everything, customers, benefit

### Resumo baseado na transcript

so hello we're excited to be giving this talk thanks for coming um this is how and why you should adopt and expose open source interfaces and the slides uh should be available on the site if you want to follow along so today in half an hour we will go over our journey adopting otel and Prometheus um how we did it and what we learned from it so our hope is if you're someone with a system that you're looking to make Prometheus compatible maybe this will give

### Excerpt da transcript

so hello we're excited to be giving this talk thanks for coming um this is how and why you should adopt and expose open source interfaces and the slides uh should be available on the site if you want to follow along so today in half an hour we will go over our journey adopting otel and Prometheus um how we did it and what we learned from it so our hope is if you're someone with a system that you're looking to make Prometheus compatible maybe this will give you some ideas about what you can do so first we'll introduce ourselves we're both from Google Cloud monitoring in New York um I'm shishi I've been a software engineer at Google for about 10 years and I really enjoy distributed systems and weird query behaviors and this is Daniel hello everyone my name is Daniel I've been at Google for almost two years a little fun fact about me I've been coding for over half my life it's something I'm very passionate about um I love solving hard problems and I'm excited to show you how we solve this one of course there are many others who are part of this project and we just wanted to mention a few of them I mean we all know who did the real work so we'll start by sharing a little story Daniel do you remember what life was like back in 2020 o yeah uh Google Cloud monitoring was not very fun uh not to say it was primitive but it was very limiting uh and let me show you exactly what I mean by that so let's start with the ingestion side and this is the side that exports your metrics and sends them to Google plan monitoring um on the ingestion side we have uh custom push based API this means if you want to um send metrics to Google Cloud monitoring um you have to import our our uh client SDK um and this is a lot of work you have to do this all programmatically um so it's a very high barrier to uh on the underlying storage side um we use Monarch which is Google's Planet scale time series if you're unfamiliar with Monarch there is a paper available um and the reason I bring this up is because this has implications uh on the API layer so for example um Monarch is schema full and this means that you have to describe what your what Your metrics look like before you can send them to um Google Cloud monitoring um and we we will talk more about these pain points later because they do become relevant later on um but for now let me talk about uh the query side uh and as you can see um you have to learn mql or you have to use the UI for this so again this is another uh investment that
