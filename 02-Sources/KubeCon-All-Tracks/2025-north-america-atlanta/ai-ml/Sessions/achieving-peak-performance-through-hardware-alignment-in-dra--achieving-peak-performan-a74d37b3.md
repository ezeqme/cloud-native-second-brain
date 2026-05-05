---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Gaurav Ghildiyal", "Google", "Byonggon Chun", "Fluidstack"]
sched_url: https://kccncna2025.sched.com/event/27Fds/achieving-peak-performance-through-hardware-alignment-in-dra-gaurav-ghildiyal-google-byonggon-chun-fluidstack
youtube_search_url: https://www.youtube.com/results?search_query=Achieving+Peak+Performance+Through+Hardware+Alignment+in+DRA+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Achieving Peak Performance Through Hardware Alignment in DRA - Gaurav Ghildiyal, Google & Byonggon Chun, Fluidstack

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Gaurav Ghildiyal, Google, Byonggon Chun, Fluidstack
- Schedule: https://kccncna2025.sched.com/event/27Fds/achieving-peak-performance-through-hardware-alignment-in-dra-gaurav-ghildiyal-google-byonggon-chun-fluidstack
- Busca YouTube: https://www.youtube.com/results?search_query=Achieving+Peak+Performance+Through+Hardware+Alignment+in+DRA+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Achieving Peak Performance Through Hardware Alignment in DRA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fds/achieving-peak-performance-through-hardware-alignment-in-dra-gaurav-ghildiyal-google-byonggon-chun-fluidstack
- YouTube search: https://www.youtube.com/results?search_query=Achieving+Peak+Performance+Through+Hardware+Alignment+in+DRA+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MjVtNltfwhc
- YouTube title: Achieving Peak Performance Through Hardware Alignment in DRA - Gaurav Ghildiyal & Byonggon Chun
- Match score: 0.875
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/achieving-peak-performance-through-hardware-alignment-in-dra/MjVtNltfwhc.txt
- Transcript chars: 24678
- Keywords: gpu, memory, actually, aligned, alignment, performance, driver, hardware, within, benchmarks, trying, usually, access, specific, misaligned, solution, network, possible

### Resumo baseado na transcript

Uh hello everyone good afternoon and thanks a lot for joining us here in this session on achieving peak performance through hardware alignment in DRRA. My name is Gorov and I'm a software engineer at Google where I work with the GK networking team. You try to run these benchmarks again and it seems like well the performance isn't consistent. So it seems like in the worst case the performance of these nickel benchmarks is dropping to as low as 41% of what you actually could get which is the maximum. Um but as the demand of computing power increased so we moved to an architecture with one shared memory and many CPUs. So in that case performance suffers due to the memory contention in terms of latency.

### Excerpt da transcript

Uh hello everyone good afternoon and thanks a lot for joining us here in this session on achieving peak performance through hardware alignment in DRRA. My name is Gorov and I'm a software engineer at Google where I work with the GK networking team. Recently I have also been working on some aspects related to DRA and have been involved with this new project called DR net which I'll also talk about soon. >> Yeah. Um hi I'm Bang. I'm currently working for fluid stack. Yeah, we run um large GPU plate and we also started building large of data centers. Yep, that's it. Okay, let's kick this off. So, uh to set the scene, your team has invested heavily on acquiring some GPU and TPU nodes. You have deployed your Kubernetes cluster on top of those GPU and TPU nodes, and you're now ready to deploy your a IML application. And after deploying your application, you're trying to run some benchmarks. Well, the results so far look promising. We are trying to run some standard nickel benchmarks and it seems like the performance that you're getting is what you'd usually expect.

You try to run these benchmarks again and it seems like well the performance isn't consistent. So it seems like in the worst case the performance of these nickel benchmarks is dropping to as low as 41% of what you actually could get which is the maximum. In order to understand this we'll have to look at a few different things. So the agenda for this meeting today is we'll first of all discuss what modern hardware topologies is what modern hardware looks like. After that we'll discuss the problems of misalignment. basically how these modern topologies could influence this alignment behavior. We'll look at DRA as the solution towards solving many of these alignment issues. We'll cover a few cases where we have performed some benchmarks and discuss what those benchmarking numbers look like that are impacted by this alignment. And then we'll actually just discuss some best practices and a more future outlook on what is happening in the community right now. Okay, before we go further, um let me briefly give some overview of MON hardware topologies.

So this is what we really had at the very beginning. So one CPU, one memory as it is pretty simple and straightforward. Um but as the demand of computing power increased so we moved to an architecture with one shared memory and many CPUs. However, people quickly found that there was some contention between CPUs um yeah contention between CPUs trying to access
