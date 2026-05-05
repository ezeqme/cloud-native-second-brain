---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability"]
speakers: ["Bryan Boreham"]
source_url: https://promcon.io/2025-munich/talks/cpu-hardware-counters/
youtube_url: https://www.youtube.com/watch?v=AtFDF9gUObo
youtube_search_url: https://www.youtube.com/results?search_query=CPU+Hardware+Counters+PromCon+2025
video_match_score: 0.894
status: video-found
---

# CPU Hardware Counters

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: Bryan Boreham
- Página oficial: https://promcon.io/2025-munich/talks/cpu-hardware-counters/
- YouTube: https://www.youtube.com/watch?v=AtFDF9gUObo

## Resumo

Counters are a fundamental unit of monitoring in Prometheus: how many requests were processed, how many CPU-seconds consumed, how many bytes sent over a network. These counters are exposed either by the application being monitored or by the operating system. But there are also counters inside the CPU itself, such as number of cache hits, number of RAM accesses, number of instructions processed.

## Abstract oficial

Counters are a fundamental unit of monitoring in Prometheus: how many requests were processed, how many CPU-seconds consumed, how many bytes sent over a network. These counters are exposed either by the application being monitored or by the operating system.

But there are also counters inside the CPU itself, such as number of cache hits, number of RAM accesses, number of instructions processed. These can give an amazingly detailed view of how the system is performing.

Historically it was impossible to get at CPU-level counters on cloud servers, as they were hidden by the hypervisor. But in the few years, CPU manufacturers and cloud providers have added interfaces to bridge this gap

This talk looks at:


What kinds of CPU counters are most useful.
When you can get access to CPU counters on cloud servers.
How to get those counters into Prometheus.


We will focus on the Linux operating system.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/cpu-hardware-counters/
- YouTube: https://www.youtube.com/watch?v=AtFDF9gUObo
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AtFDF9gUObo
- YouTube title: PromCon 2025 - CPU Hardware Counters
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/cpu-hardware-counters/AtFDF9gUObo.txt
- Transcript chars: 23802
- Keywords: counters, hardware, basically, memory, actually, misses, exporter, running, prometheus, instructions, container, numbers, pretty, metrics, virtual, hypervisor, advisor, getting

### Resumo baseado na transcript

Um I have worked on uh Prometheus and adjacent projects for about eight years now and I'm a um maintainer of Prometheus. I'm just going to tell you about a thing that you might like to do and what you can do with it. Um, so I've drawn a CPU at the bottom of the picture and a Prometheus at the top of the picture. Um, and then we need some kind of exporter to get it into Prometheus format. And um uh you can um tell it to be not so paranoid and let people see the performance counters by changing this uh uh cyscodal or proc file. If it's um if it's inside a container, you might need some other uh uh privileges or or um uh security profile.

### Excerpt da transcript

[music] Hello. Everyone hear me? All right. Well, welcome. Uh, so thanks for coming back to day two of PromCon. Um, my name is Brian Borum. Let's put that up on the next slide. Uh, I work at Graphana Labs. Um I have worked on uh Prometheus and adjacent projects for about eight years now and I'm a um maintainer of Prometheus. Um but today uh today I'm I'm talking about way down in the hardware. Um and uh so there's no uh there's no AI in this talk. Uh there's no uh there's no demo uh because I was too scared. Um and uh in some sense I didn't really do anything. I mean I I well you'll you'll see you'll see what I did. I'm just going to tell you about a thing that you might like to do and what you can do with it. Um okay. So uh well let's start counters. Um so I think I'm about the fifth talk to put up a slide like this. Uh like uh you know Prometheus is is pretty keen on counters. Um and and this is example uh which is counting how many bytes has this network interface received. Um so so counters are a thing that are found all over the place in in operating systems and applications and uh uh devices and so on.

So um so yeah there there's billions of them. Um how many seconds has this process executed on CPU is a is another popular counter. Um and and that one leads us to CPU is busy. Um, and I, you know, why do I do this job? Because I I basically spend most of my time st shouting at the screen like, well, what is it doing? Okay, it's busy doing what? Um, you know, the CPU could be doing arithmetic. Maybe that's what you expect, but it it might also be waiting for memory. memory is is much much slower than um than the the the arithmetic bit of the CPU. Um or if you kind of understand the complicated bits that could be the the instruction pipeline could have flushed after a mispredicted branch. Um so uh what can we get that extra level of detail is essentially what this talk is about. Um so this is CPU We'll be going through this. No. Uh, this is a Intel Xeon Skylake. Um, it is a 28 core, I think. Um, so, so what something that looks a bit like this is a core. Uh, and they're kind of mirror imaged as they go across.

Um so that's the kind of hardware I'm talking about. Um other CPUs are available. Uh basically the same facilities are available on um Intel, AMD, ARM. Uh it tends to be on the server parts. Um maybe maybe less so on the desktop parts. All right. So uh so this picture is going to be a little bit complicated to walk through. Uh so I simplified it
