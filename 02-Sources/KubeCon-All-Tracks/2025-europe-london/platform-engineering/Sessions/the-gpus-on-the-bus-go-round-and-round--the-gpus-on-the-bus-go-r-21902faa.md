---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Natalie Bandel", "Ryan Hallisey", "NVIDIA"]
sched_url: https://kccnceu2025.sched.com/event/1tx7H/the-gpus-on-the-bus-go-round-and-round-natalie-bandel-ryan-hallisey-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=The+GPUs+on+the+Bus+Go+%E2%80%98Round+and+%E2%80%98Round+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The GPUs on the Bus Go ‘Round and ‘Round - Natalie Bandel & Ryan Hallisey, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Natalie Bandel, Ryan Hallisey, NVIDIA
- Schedule: https://kccnceu2025.sched.com/event/1tx7H/the-gpus-on-the-bus-go-round-and-round-natalie-bandel-ryan-hallisey-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=The+GPUs+on+the+Bus+Go+%E2%80%98Round+and+%E2%80%98Round+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The GPUs on the Bus Go ‘Round and ‘Round.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7H/the-gpus-on-the-bus-go-round-and-round-natalie-bandel-ryan-hallisey-nvidia
- YouTube search: https://www.youtube.com/results?search_query=The+GPUs+on+the+Bus+Go+%E2%80%98Round+and+%E2%80%98Round+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cLJRh4y4vXg
- YouTube title: The GPUs on the Bus Go ‘Round and ‘Round - Natalie Bandel & Ryan Hallisey, NVIDIA
- Match score: 0.759
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-gpus-on-the-bus-go-round-and-round/cLJRh4y4vXg.txt
- Transcript chars: 22117
- Keywords: gpu, reboot, capacity, device, failures, workloads, driver, actually, failure, challenges, clusters, process, little, working, workload, problems, issues, devices

### Resumo baseado na transcript

I'm going to do my best to see, but I need some help from the audience. Uh, if you have had to restart a machine because a GPU wasn't working the way you'd hoped. Uh so when we when we actually started our our journey when we were looking at um trying to understand and achieve that goal of having maximum capacity we wanted to we wanted we needed to understand um well we actually we ran into some problems. So the first step to solve the problem is to acknowledge the problem exist. First part is custom GPU problem detector and we use an internal GPU device plug-in. When it detects the problem, it marks the node and putting a condition on the node.

### Excerpt da transcript

Okay, we're going to get started. Holy cow, I can't see anything back there. These lights are bright. Okay, really quick exercise. I'm going to do my best to see, but I need some help from the audience. Can you raise your hand if you have ever had a GPU fall off the bus? I can't really see. I see a few. There are some hands. Yeah. All right, keep your hands raised for a second. Uh, if you have had to restart a machine because a GPU wasn't working the way you'd hoped. How many more hands? Oh, even more. Okay, quite a few. Okay, you can put your hands down. Thank you. Okay. Um, so we're from NVIDIA. I'm Ryan Haly. This is Natalie Bandelle. Um, and we encounter this too. I had my hand raised. She had her hand raised. We experience this a lot. Um, and uh, so we we feel your pain on this. We this is something that uh we're going to be talking about how how we deal with this. Uh we run Kubernetes clusters and we have a lot of GPUs and we go through the same thing. We will reboot our GPUs for for different various reasons.

So that's what we're going to talk about. Okay. So a little bit about our uh our Kubernetes clusters. Um we've got a large fleet. We've got uh geoloccated all over the world. Um so pretty much in we're in a lot of countries uh 40 plus clusters 30,000 plus nodes uh 60,000 plus GPUs so roughly two GPUs uh two GPUs per node of density uh and like I said we run into a lot of device failures so that's a lot of GPUs so we do encounter this okay so the product that uh that we actually represent we build the infrastructure for it's called GeForce Now it's I think Nvidia cloud gaming. Um so we want to take graphics and we want to stream these to the end user. So we want low latency, you know, we're geollocated right near the the user. Um and we want to give that that uh desktop experience uh for the GPU like you're playing the game locally. Um so our workload uh primarily when representing uh and working with uh GeForce Now is we have a lot of online gaming like I said and we also do a bit of inferencing uh we have spot capacity um so we'll run some inferencing workloads uh there with our additional capacity um so we'll we'll fill our data centers quite a bit.

Okay, so device failures. Um, so we want to maintain our capacity, right? It's really important. We want our GPUs running really hot. They they cost us a lot of money. We put a lot of effort into putting them into the data center and we want them used. Um, so that's a really important thing and
