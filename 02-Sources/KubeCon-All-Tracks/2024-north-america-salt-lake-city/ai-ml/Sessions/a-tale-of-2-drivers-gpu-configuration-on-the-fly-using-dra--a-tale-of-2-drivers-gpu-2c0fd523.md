---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Alay Patel", "Varun Ramachandra Sekar US", "Nvidia"]
sched_url: https://kccncna2024.sched.com/event/1i7lw/a-tale-of-2-drivers-gpu-configuration-on-the-fly-using-dra-alay-patel-varun-ramachandra-sekar-us-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=A+Tale+of+2+Drivers%3A+GPU+Configuration+on+the+Fly+Using+DRA+CNCF+KubeCon+2024
slides: []
status: parsed
---

# A Tale of 2 Drivers: GPU Configuration on the Fly Using DRA - Alay Patel & Varun Ramachandra Sekar US, Nvidia

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Alay Patel, Varun Ramachandra Sekar US, Nvidia
- Schedule: https://kccncna2024.sched.com/event/1i7lw/a-tale-of-2-drivers-gpu-configuration-on-the-fly-using-dra-alay-patel-varun-ramachandra-sekar-us-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=A+Tale+of+2+Drivers%3A+GPU+Configuration+on+the+Fly+Using+DRA+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre A Tale of 2 Drivers: GPU Configuration on the Fly Using DRA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lw/a-tale-of-2-drivers-gpu-configuration-on-the-fly-using-dra-alay-patel-varun-ramachandra-sekar-us-nvidia
- YouTube search: https://www.youtube.com/results?search_query=A+Tale+of+2+Drivers%3A+GPU+Configuration+on+the+Fly+Using+DRA+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xE_no5_6Ie0
- YouTube title: A Tale of 2 Drivers: GPU Configuration on the Fly Using DRA- Alay Patel & Varun Ramachandra Sekar US
- Match score: 0.833
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/a-tale-of-2-drivers-gpu-configuration-on-the-fly-using-dra/xE_no5_6Ie0.txt
- Transcript chars: 23285
- Keywords: gpu, device, resource, devices, plugins, attribute, workload, resources, template, workloads, plugin, multiple, aligned, running, advertised, allocated, important, geforce

### Resumo baseado na transcript

hello everyone I'm um I'm Von sear and this is my colleague Al we're both from Nvidia and we are part of the GeForce now Cloud um our talk is a tale of two drivers so let's get started so in our talk we're going to talk about what GeForce now cloud is what are the use cases we're trying to solve for it um how we run GPU workloads with Device plugins what are the problems we see with it and then how do ra uh solves a lot

### Excerpt da transcript

hello everyone I'm um I'm Von sear and this is my colleague Al we're both from Nvidia and we are part of the GeForce now Cloud um our talk is a tale of two drivers so let's get started so in our talk we're going to talk about what GeForce now cloud is what are the use cases we're trying to solve for it um how we run GPU workloads with Device plugins what are the problems we see with it and then how do ra uh solves a lot of our issues and then we'll end our talk with the demo and we'll have some QA after that so gForce now is a cloud gaming service that enables end users to run games on the cloud and we run our Cloud on the kubernetes stack and we use a bunch of Open Source uh to enable us so we use Cube work for VM management we use aen kubernetes for our cni fluent bit Prometheus for our observability and then Opa and gatekeeper for policy management and we have a pretty big scale we run about 40 data centers with about 30,000 nodes and 60,000 gpus and then we run about a million VMS daily so I said we run virtual machines but uh kubernetes doesn't support it so we have cuboard which runs VMS as part of kubernetes and then this VM is just a custom resource that Cube word translates it into a pod and then it runs the uh your it runs the virtual machine using the KVM hypervisor on the nodes so some of the use cases that we have are let's say you're a user and you want to play games with the highest FPS that is possible and you want to have the highest Graphics that your games can support so the the way we run it for you is we'd spin up a very large VM and we'll give it a full GPU and do a pass through of the GPU to your VM and then we'll stream your game uh from our data center to your compter computer now if you don't want that and you just want uh let's say 60 FPS and just about 1080p resolutions then we'd spin up a much smaller VM we'll give it like half a GPU and then we'll stream it to you and then if you just want to try what GeForce now is then we'll run a really small VM and then give it a quarter GPU and and then you can play around and try to see what GeForce now offers but when you play games we all know that uh these games are very lag sensitive you don't want your games to stter if your experience needs to be good these virtual machines that we run for you need to be highly optimized for performance so what we have to do is uh get all the virtual machine to be fully fully tuned for for Optimal Performance yeah so we have all these use cases and
