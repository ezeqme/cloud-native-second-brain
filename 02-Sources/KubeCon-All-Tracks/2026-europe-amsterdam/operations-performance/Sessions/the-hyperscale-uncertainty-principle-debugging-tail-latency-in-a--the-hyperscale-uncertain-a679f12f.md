---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Yashraj Kakkad", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2CW3k/the-hyperscale-uncertainty-principle-debugging-tail-latency-in-a-trillion-object-system-yashraj-kakkad-google
youtube_search_url: https://www.youtube.com/results?search_query=The+Hyperscale+Uncertainty+Principle%3A+Debugging+Tail+Latency+in+a+Trillion-Object+System+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The Hyperscale Uncertainty Principle: Debugging Tail Latency in a Trillion-Object System - Yashraj Kakkad, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yashraj Kakkad, Google
- Schedule: https://kccnceu2026.sched.com/event/2CW3k/the-hyperscale-uncertainty-principle-debugging-tail-latency-in-a-trillion-object-system-yashraj-kakkad-google
- Busca YouTube: https://www.youtube.com/results?search_query=The+Hyperscale+Uncertainty+Principle%3A+Debugging+Tail+Latency+in+a+Trillion-Object+System+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The Hyperscale Uncertainty Principle: Debugging Tail Latency in a Trillion-Object System.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW3k/the-hyperscale-uncertainty-principle-debugging-tail-latency-in-a-trillion-object-system-yashraj-kakkad-google
- YouTube search: https://www.youtube.com/results?search_query=The+Hyperscale+Uncertainty+Principle%3A+Debugging+Tail+Latency+in+a+Trillion-Object+System+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hpFqElHNLaY
- YouTube title: The Hyperscale Uncertainty Principle: Debugging Tail Latency in a Trillion-Object... Yashraj Kakkad
- Match score: 0.981
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-hyperscale-uncertainty-principle-debugging-tail-latency-in-a-trill/hpFqElHNLaY.txt
- Transcript chars: 25881
- Keywords: partitions, pipeline, probably, storage, number, shards, generally, object, framework, metadata, thought, workers, underlying, systems, happen, request, always, latency

### Resumo baseado na transcript

I'm going to talk about what happens when an elegant, perfectly balanced design collides with brutal physical reality of underlying systems and bare metal. The challenge that I'm going to talk about is that of referential integrity. Uh so, not surprisingly, even the best batch processing frameworks that you see break at this scale because of like various issues in the underlying systems and things like that. Uh so, what we did was we we designed what we thought is like the perfect blueprint for this kind of a problem. Despite a uniform design, uh runtimes were very unpredictable with very very high worst-case actuals. Um one is that of course, like I mean, there is storage overhead, garbage collection is happening at a slower pace, and therefore, we are having objects around longer than we need.

### Excerpt da transcript

My name is Yashraj Gakkad. I'm a software engineer at Google Photos. I'm going to talk about what happens when an elegant, perfectly balanced design collides with brutal physical reality of underlying systems and bare metal. So, let's talk about tail latency. So, at Google Photos, we operate at an exabyte scale footprint. We have trillions of objects in our systems. And this is massive scale even by our own standards. So, at this scale, we are not just thinking about storage. We are looking at managing memory at a planetary scale. So, storing the bytes undoubtedly is a challenge. But, there is a lot more. The challenge that I'm going to talk about is that of referential integrity. So, we have a massive relational metadata database and this relational metadata database is perfectly in sync with an object storage system. Of course, objects which are referenced by the metadata storage have to be referenced by the metadata storage system. And this metadata system has to operate as a source of truth. So, if an object is referenced by this metadata storage system, it has to exist in the object storage system.

If it is if it does not exist, we have a problem. And vice versa as well. If an object is not referenced by this metadata system, it's it's it's an object that we no longer need in our system. And and we we for various reasons need to like clear it off as soon as possible. So, yeah, I mean, this is like just a foreign key, but it's across two different databases and it's at trillions of objects of scale. So, there is nothing out of the box which exists for something like this. And to verify this consistency, um like basically doing both these things, like detecting data loss as well as doing garbage collection, uh we run a very huge concurrency pipeline. And this is kind of like the basis of uh most of this talk. So, yes, um I mean, we have a pipeline. Uh we need to verify trillions of objects. And for various reasons, we need to read uh the entirety of the two data sources when we do this verification. So, yes, obviously Okay. Um so, yeah, obviously, we are going to need um massive massive amount of parallelism to do this.

Uh so, not surprisingly, even the best batch processing frameworks that you see break at this scale because of like various issues in the underlying systems and things like that. I mean, things just keep breaking. Uh so, what we did was we we designed what we thought is like the perfect blueprint for this kind of a problem. Um so, we j
