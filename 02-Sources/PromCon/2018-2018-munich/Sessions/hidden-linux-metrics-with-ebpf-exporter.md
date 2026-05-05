---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/hidden-linux-metrics-with-ebpf-exporter/
youtube_url: https://www.youtube.com/watch?v=dRdJ75tKZak
youtube_search_url: https://www.youtube.com/results?search_query=Hidden+Linux+Metrics+with+ebpf_exporter+PromCon+2018
video_match_score: 0.987
status: video-found
---

# Hidden Linux Metrics with ebpf_exporter

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/hidden-linux-metrics-with-ebpf-exporter/
- YouTube: https://www.youtube.com/watch?v=dRdJ75tKZak

## Resumo

Speaker: Ivan Babrou While there are plenty of readily available metrics for monitoring the Linux kernel, many gems remain hidden. With the help of recent developments in eBPF, it is now possible to run safe programs in the kernel to collect arbitrary information with little to no overhead. A few examples include: Disk latency and IO size histograms Run queue (scheduler) latency Page cache efficiency Directory cache efficiency LLC (aka L3 cache) efficiency Kernel timer counters System-wide TCP retransmits Practically any event from "perf list" output and any kernel function can be traced, analyzed, and turned into a metric with almost arbitrary labels attached to it.

## Abstract oficial

Speaker: Ivan Babrou

While there are plenty of readily available metrics for monitoring the Linux kernel, many gems remain hidden. With the help of recent developments in eBPF, it is now possible to run safe programs in the kernel to collect arbitrary information with little to no overhead. A few examples include:


Disk latency and IO size histograms
Run queue (scheduler) latency
Page cache efficiency
Directory cache efficiency
LLC (aka L3 cache) efficiency
Kernel timer counters
System-wide TCP retransmits


Practically any event from "perf list" output and any kernel function can be traced, analyzed, and turned into a metric with almost arbitrary labels attached to it.

If you are already familiar with BCC tools, you may think of ebpf_exporter as BCC tools turned into Prometheus metrics.

In this talk we'll go over eBPF basics, how to write programs and get insights into a running system.

https://github.com/cloudflare/ebpf_exporter



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/hidden-linux-metrics-with-ebpf-exporter/
- YouTube: https://www.youtube.com/watch?v=dRdJ75tKZak
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dRdJ75tKZak
- YouTube title: PromCon 2018: Hidden Linux Metrics with ebpf_exporter
- Match score: 0.987
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/hidden-linux-metrics-with-ebpf-exporter/dRdJ75tKZak.txt
- Transcript chars: 21311
- Keywords: kernel, metrics, exporter, second, memory, histograms, machine, operations, histogram, events, prometheus, useful, instead, write, programs, production, latency, overhead

### Resumo baseado na transcript

so I work for a company called CloudFlare so where I focus on performance and efficiency of our products I don't usually do public speaking and I have terrible memory so please forgive me if I look at the notes too much so if you never heard about CloudFlare it means one of two things either you own a website and we fail to inform you that you should totally use us or you don't own a website and we're working well enough for you to dun know that we're

### Excerpt da transcript

so I work for a company called CloudFlare so where I focus on performance and efficiency of our products I don't usually do public speaking and I have terrible memory so please forgive me if I look at the notes too much so if you never heard about CloudFlare it means one of two things either you own a website and we fail to inform you that you should totally use us or you don't own a website and we're working well enough for you to dun know that we're we exist we're a CDN with benefits so in additional to traditional caching and DDoS protection and like bringing content closer to the user we try to be the forefront of innovation with technologies like TLS 1.3 quick server push edge workers and the idea is generally to make Internet the more secure and up-to-date for everyone even if your origin server does not support these technologies we're also the fastest authority of DNS and we provide privacy oriented one that one that one dot one resolver so you should totally use that and you should totally use that with DNS over TLS so you're I speak don't see what you're browsing on the internet and Prometheus and prom Khan website also uses apparently last year my colleague Matt Bostick was here he was talking how we do planet-scale edge not network monitoring with promises and you can check the slides in the video it's still useful I'm just gonna give a quick refresher on on the numbers so the only thing that didn't change here is the 10% number and it's a it's not exactly scientific number it depends on how you count the internet requests otherwise we doubled in terms of HTTP and DNS requests and DNS does not include the public one dot one dot one dot one resolver so that did grow by a factor of infinity we're at 150 data centers and instead of a hundred just a year ago and we plan to cross 200 this year and what each of those needs monitoring and that's what we use operators for and our global Prometheus deployment did grow with with our H Network the numbers here are per Prometheus so they not for all 267 Prometheus services and we're very much looking forward to having tennis to manage this and keep this in check so that's all great but that's not what I was here to talk about so I want to tell about an exporter so let's first have a look at what do we have now so there are two main exporters one can use for system metrics with promises on Linux so the first one is not exported gives you information about basics like CPU usage breakdown by type memory usage
