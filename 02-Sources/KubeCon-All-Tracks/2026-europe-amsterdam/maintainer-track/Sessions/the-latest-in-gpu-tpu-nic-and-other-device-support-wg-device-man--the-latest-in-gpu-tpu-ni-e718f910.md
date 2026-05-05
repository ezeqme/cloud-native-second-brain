---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["John Belamaric", "Google", "Patrick Ohly", "Intel"]
sched_url: https://kccnceu2026.sched.com/event/2EIbN/the-latest-in-gpu-tpu-nic-and-other-device-support-wg-device-management-john-belamaric-google-patrick-ohly-intel
youtube_search_url: https://www.youtube.com/results?search_query=The+Latest+in+GPU%2C+TPU%2C+NIC+and+Other+Device+Support+-+WG+Device+Management+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The Latest in GPU, TPU, NIC and Other Device Support - WG Device Management - John Belamaric, Google & Patrick Ohly, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: John Belamaric, Google, Patrick Ohly, Intel
- Schedule: https://kccnceu2026.sched.com/event/2EIbN/the-latest-in-gpu-tpu-nic-and-other-device-support-wg-device-management-john-belamaric-google-patrick-ohly-intel
- Busca YouTube: https://www.youtube.com/results?search_query=The+Latest+in+GPU%2C+TPU%2C+NIC+and+Other+Device+Support+-+WG+Device+Management+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The Latest in GPU, TPU, NIC and Other Device Support - WG Device Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EIbN/the-latest-in-gpu-tpu-nic-and-other-device-support-wg-device-management-john-belamaric-google-patrick-ohly-intel
- YouTube search: https://www.youtube.com/results?search_query=The+Latest+in+GPU%2C+TPU%2C+NIC+and+Other+Device+Support+-+WG+Device+Management+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MAwL8A1WCjw
- YouTube title: The Latest in GPU, TPU, NIC and Other Device Support - WG Device Ma... John Belamaric & Patrick Ohly
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-latest-in-gpu-tpu-nic-and-other-device-support-wg-device-managemen/MAwL8A1WCjw.txt
- Transcript chars: 28081
- Keywords: resource, device, resources, devices, driver, working, gpu, hardware, scheduling, actually, native, around, meeting, available, already, feature, management, another

### Resumo baseado na transcript

This is another update of the working group device management meeting, also sometimes known as the working group where we do dynamic resource allocation. I've been with DRA since the very beginning uh writing the initial caps. It's not just one sik that can own this is a it's a core change in kubernetes that has lots of different stakeholders starting with architecture autoscaling network node and very much a lot of things are scheduling related because we want the right choice for different parts to really land optimally. So what we have right now in terms of solving this problem that I just alluded to, it starts out with the resource slice API describing devices available on nodes or for nodes in the cluster. So, um, yeah, what what we we've got a lot of a lot of things going on and I'll show you a little more detail in a minute, but at a at a high level, some of the problems we're working to solve um relate to uh alignment within the node. So if you have multiple devices, you have your GPU, you have your um your nick, you have your CPU, uh we want to make sure that within the node um those things all uh line up and so uh you get optimal performance.

### Excerpt da transcript

Okay, well, we have a few more seconds. We're getting ready. Doors closing. Last chance. Okay, let's get started. Welcome everyone. This is another update of the working group device management meeting, also sometimes known as the working group where we do dynamic resource allocation. So, let me introduce your hosts, your co-chairs today. Um, my name is Patrick Uli. I'm a principal engineer working for Intel on Kubernetes. I've been with DRA since the very beginning uh writing the initial caps. Presenting today with me is John Bellame from Google. He joined us when we started the working group and is very good at coming up with all kinds of odds ideas where I have to tell him that well this is crazy we can't do that and then we figure out how to do it anyway. Also another chair is Kevin Glu distinguished engineer at Nvidia here in the front row. uh he is covering the driver side to some extent and sign node. So we all collaborated together on this and nowadays we have lots more lot of lot more people involved than in the beginning.

We'll you'll get to see some of that uh as part of this presentation. Yeah. Um I'm assuming that you kind of know what we do, but let's let me repeat it anyway. So we came together to solve a problem of really how to make it simpler to manage accelerators in Kubernetes. We were unhappy with the device plug-in interface and wanted to have a better way to configure hardware to describe hardware, how to to allocate it in a more flexible way. And that's what led to dynamic resource allocation as a kind of alternative to device plugins. And then sometime later interest uh grew and we formally founded the working group to host this because it is really a crosscutting affair. It's not just one sik that can own this is a it's a core change in kubernetes that has lots of different stakeholders starting with architecture autoscaling network node and very much a lot of things are scheduling related because we want the right choice for different parts to really land optimally. So a lot of lot of things actually have been going on in six scheduling around that.

We have successfully delivered DRA. It is GA for a while now. Um well okay well that's old news. Uh just to recap. So what we have right now in terms of solving this problem that I just alluded to, it starts out with the resource slice API describing devices available on nodes or for nodes in the cluster. That's the information that gets published by a DRA driver. The users don't ne
