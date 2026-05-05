---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Ajay Sundar Karuppasamy", "Google LLC", "Itamar Holder", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27FfE/deep-dive-handling-kubernetes-memory-pressure-achieving-workload-stability-with-nodeswap-ajay-sundar-karuppasamy-google-llc-itamar-holder-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Deep+Dive%3A+Handling+Kubernetes+Memory+Pressure+%26+Achieving+Workload+Stability+With+NodeSwap+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Deep Dive: Handling Kubernetes Memory Pressure & Achieving Workload Stability With NodeSwap - Ajay Sundar Karuppasamy, Google LLC & Itamar Holder, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Ajay Sundar Karuppasamy, Google LLC, Itamar Holder, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27FfE/deep-dive-handling-kubernetes-memory-pressure-achieving-workload-stability-with-nodeswap-ajay-sundar-karuppasamy-google-llc-itamar-holder-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Deep+Dive%3A+Handling+Kubernetes+Memory+Pressure+%26+Achieving+Workload+Stability+With+NodeSwap+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Deep Dive: Handling Kubernetes Memory Pressure & Achieving Workload Stability With NodeSwap.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FfE/deep-dive-handling-kubernetes-memory-pressure-achieving-workload-stability-with-nodeswap-ajay-sundar-karuppasamy-google-llc-itamar-holder-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Deep+Dive%3A+Handling+Kubernetes+Memory+Pressure+%26+Achieving+Workload+Stability+With+NodeSwap+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bFrEPfls5PQ
- YouTube title: Deep Dive: Handling Kubernetes Memory Pressure & Achievi... Ajay Sundar Karuppasamy, & Itamar Holder
- Match score: 0.773
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/deep-dive-handling-kubernetes-memory-pressure-achieving-workload-stabi/bFrEPfls5PQ.txt
- Transcript chars: 27061
- Keywords: memory, kernel, pressure, another, basically, activity, swapping, workload, actually, better, around, limits, watermark, tuning, process, eviction, generally, control

### Resumo baseado na transcript

So um yeah, as I said, it's um a great pleasure being here in CubeCon and thank you all for coming. Um we have a bit of a long uh title for our talk, but basically we're going to talk about optimizing swap. Um so one of the problems or challenges with swap is that it requires a lot of um configuration and tuning and this is something that cublet cannot do for you because cublet runs in a very limited scope. So obviously control plane nodes are crucial and degrading performance could be could have uh dramatic effects. Um, another question is should you um allow uh system demons to use swap? Um, it it makes total sense that some of your system level demons uh would be great candidate for swaps for swap.

### Excerpt da transcript

So um yeah, as I said, it's um a great pleasure being here in CubeCon and thank you all for coming. Um we have a bit of a long uh title for our talk, but basically we're going to talk about optimizing swap. Um so I'm from Red Hat. My friend here is AJ from Google and uh I had the privilege to uh lead swap development until uh uh graduation, which is something that I'm super excited about. But um let me tell you this was not easy at all. So um when I started looking at swap it was in the 126 era um and back then swap was only supported um in an alpha and was very experimental and initial implementation and the developer that started it soon uh after left the project. So there was no real development or any interest around it. Um so um I had to um gain interest around it um prioritize it and basically convince people uh this is important. Uh but even then people are rightfully uh very cautious about this because it's such a fundamental change in uh Kubernetes. So as you can see um it has been many releases and many beta versions but I'm very excited that it finally had reached uh full graduation.

And one of the things that allowed it to uh graduate eventually is that we have framed it as a basic swap enablement feature. So um we understand that there's more work to be done in order for the feature to be complete and we are already working on three follow-up enhancements. Um this is a great time to collaborate. Um so if you have if you want to uh you're welcome. U basically we're working about pod level swap controls and making evictions and scheduling uh swap aware. So that's basically the plans for the future. Um so one of the problems or challenges with swap is that it requires a lot of um configuration and tuning and this is something that cublet cannot do for you because cublet runs in a very limited scope. So it's a system demon. It cannot edit um OS configuration and certainly not hardware. That's out of scope for cublet. But that's fine because that's that when you as an admin can come into the picture and do a lot to optimize swap for your use case which is actually a real necessity with swap.

Um so generally speaking when you'd want to use swap uh you'd have to go through three phases. Um deploying it, configuring it and uh eventually you'd probably want to monitor it and uh make sure everything runs as expected. Um so let's talk about the hardware you you'd use. So when I um started dealing with swap, I basically um treated uh swap as a safety ne
