---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core", "SRE Reliability"]
speakers: ["Alay Patel", "Ryan Hallisey", "NVIDIA"]
sched_url: https://kccnceu2025.sched.com/event/1tx8v/scaling-gpu-clusters-without-melting-down-alay-patel-ryan-hallisey-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+GPU+Clusters+Without+Melting+Down%21+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Scaling GPU Clusters Without Melting Down! - Alay Patel & Ryan Hallisey, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Alay Patel, Ryan Hallisey, NVIDIA
- Schedule: https://kccnceu2025.sched.com/event/1tx8v/scaling-gpu-clusters-without-melting-down-alay-patel-ryan-hallisey-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+GPU+Clusters+Without+Melting+Down%21+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Scaling GPU Clusters Without Melting Down!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8v/scaling-gpu-clusters-without-melting-down-alay-patel-ryan-hallisey-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Scaling+GPU+Clusters+Without+Melting+Down%21+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dUfp3j1j-mg
- YouTube title: Scaling GPU Clusters Without Melting Down! - Alay Patel & Ryan Hallisey, NVIDIA
- Match score: 0.799
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/scaling-gpu-clusters-without-melting-down/dUfp3j1j-mg.txt
- Transcript chars: 22884
- Keywords: server, memory, control, utilization, connections, actually, scheduleuler, workloads, requests, talking, secrets, environment, wanted, workload, started, connection, gpu, running

### Resumo baseado na transcript

Um and like I said, we're going to be talking about the Kubernetes control plane. So the the story to think about here is GPUs are being released every you know one to two years. Uh so this is a big problem for us and you can kind of see it in the picture on the right. Uh when we do these list calls it was pretty obvious um that we would just it would and you know we'd lose all our metrics for the API server. So you can use API priority fairness to say well we only want to allow two concurrent list calls to be executed and this was really helpful for us um it actually is what solved our problem and what kept us within the safe area So this is great significantly reduced ours um and and was able to get through the problem.

### Excerpt da transcript

Uh so I'm uh I'm Ryan Haly. I work at NVIDIA. This is my colleague Olay Patel. Um and like I said, we're going to be talking about the Kubernetes control plane. So the the story to think about here is GPUs are being released every you know one to two years. They're getting more and more powerful. And so more powerful means theoretically we can support more workloads. More workloads means we can have more secrets, more volumes, more objects and all this is pressure on the API server, right? So we can do all these things and what we want to do is we want to make sure our control plane, our Kubernetes control plane is still running. So we did an experiment where we wanted to as a a bare metal provider um someone who runs on bare metal Kubernetes we wanted to see if we could scale the compute independently of the control plane. So this experiment what we had in mind is we would take our control plane and we'd say okay let's have a fixed set of memory and CPU and let's scale up our compute and let's see what happens.

Um so we keep control plane resources constant and we want to see how it performs. So it went perfect right? Not exactly. I like this title incidents incidents incidents. So there's a few things that went wrong. Uh we're going to talk about three of them. I'm going to talk about the first one. Um the first one uh first big thing we encountered a large number of list calls to secrets would lead to control plane outages. And these aren't ordinary secrets, let me tell you. Can I go to the next slide here? There we go. Okay. Um, we noticed that in our environment, if we have a lot of secrets, we can run into uh an oom. Specifically, if we do list calls to the API server and so these secrets, like I said, they're not quite the ordinary secret. They're not like a base 64 encoded string that's like a few hundred bytes. They're 0.2 megabytes each. They're pretty large. And we have 5,000 of these things. So think about that in terms of CD storage. So we haved storing these things. That's okay. But now when you do a list call, think about all that information that needs to go into the API server into the cache and think about how much memory that consumes.

And so if we do two concurrent list calls, we can get a ton of this stuff built up in the cache and we can run out of memory in the API server. Uh so this is a big problem for us and you can kind of see it in the picture on the right. Uh when we do these list calls it was pretty obvious um that we would
