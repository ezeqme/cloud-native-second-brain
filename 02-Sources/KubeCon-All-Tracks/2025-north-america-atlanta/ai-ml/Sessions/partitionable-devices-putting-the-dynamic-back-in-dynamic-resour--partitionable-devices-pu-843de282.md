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
themes: ["AI ML"]
speakers: ["Morten Jæger Torkildsen", "Google", "Jan-Philip Gehrcke", "NVIDIA"]
sched_url: https://kccncna2025.sched.com/event/27FbY/partitionable-devices-putting-the-dynamic-back-in-dynamic-resource-allocation-morten-jaeger-torkildsen-google-jan-philip-gehrcke-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Partitionable+Devices%3A+Putting+the+%E2%80%9CDynamic%E2%80%9D+Back+in+Dynamic+Resource+Allocation+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Partitionable Devices: Putting the “Dynamic” Back in Dynamic Resource Allocation - Morten Jæger Torkildsen, Google & Jan-Philip Gehrcke, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Atlanta
- Speakers: Morten Jæger Torkildsen, Google, Jan-Philip Gehrcke, NVIDIA
- Schedule: https://kccncna2025.sched.com/event/27FbY/partitionable-devices-putting-the-dynamic-back-in-dynamic-resource-allocation-morten-jaeger-torkildsen-google-jan-philip-gehrcke-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Partitionable+Devices%3A+Putting+the+%E2%80%9CDynamic%E2%80%9D+Back+in+Dynamic+Resource+Allocation+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Partitionable Devices: Putting the “Dynamic” Back in Dynamic Resource Allocation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FbY/partitionable-devices-putting-the-dynamic-back-in-dynamic-resource-allocation-morten-jaeger-torkildsen-google-jan-philip-gehrcke-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Partitionable+Devices%3A+Putting+the+%E2%80%9CDynamic%E2%80%9D+Back+in+Dynamic+Resource+Allocation+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5GIDHxwQGiM
- YouTube title: Partitionable Devices: Putting the “Dynamic” Back in... Morten Jæger Torkildsen & Jan-Philip Gehrcke
- Match score: 0.778
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/partitionable-devices-putting-the-dynamic-back-in-dynamic-resource-all/5GIDHxwQGiM.txt
- Transcript chars: 24782
- Keywords: devices, device, resource, memory, gpu, actually, available, counters, physical, counter, dynamic, allocation, driver, partitioning, workload, allocated, running, partitionable

### Resumo baseado na transcript

Welcome everyone to this uh session about um partitionable devices and how it puts the dynamic back in dynamic resource allocation. I've been working on Kubernetes for seven years now and the last year of or about the last year on DRA. And what makes this solve the problem we described earlier is that devices can only be allocated if sufficient capacity is available on the counters. So um the support for that uh parts of this landed in uh 134 um the one Kubernetes which I have been integrating against and um so for dynamic make device allocation um we need a few ingredients maybe not these are implementation details but I think they're still very interesting. you know simple approaches and what I really wanted to show in this little demo is that um first of all MC devices get dynamically created and destroyed which already nice but also with this type of dynamic sharing we can actually like increase GPU Um so yeah please join the device management working group if you want to learn more or contribute to the array.

### Excerpt da transcript

Welcome everyone to this uh session about um partitionable devices and how it puts the dynamic back in dynamic resource allocation. Uh I'm Morton Torlson. I work for Google. I've been working on Kubernetes for seven years now and the last year of or about the last year on DRA. Hey, Yan Phillip. I joined Nvidia beginning of the year and so far I've been focusing on um our DRA driver. You might have heard about computer domains and recently I've been shifting my efforts towards the GPU allocation. So I can tell you some things about um dynamic allocation of MC devices which makes use of the partitionable devices part of the array. Okay. So um the reason we care about this is we want to maximize GPU utilization because GPUs are expensive and scarce. So achieving high utilization is critical like idle devices are wasted money. You don't want to buy a lot of expensive GPUs and had them sit sit idle. But also workloads are diverse. Not all workloads require a full high-end GPU. Some might require hundreds or thousands of them and some might have enough with just a fraction of a full GPU.

Um, the device plug-in API that has been used for a while only allows assigning full GPUs, which means that being able to assign like partitions or fractions of the device is difficult. Uh, there are tricks to do this, but it still requires a static partitioning of the GPU, which makes it far less useful. And yeah. >> Okay. So, um, who of you has used any sharing technology for Nvidia GPUs like time slicing, MPS? Okay. Yeah. I personally I've never used time slicing MPS whatsoever. But, you know, I'm not going into time slicing here. Um, but I want to kind of compare at the high level why like MPS and Mick and why Mick is like fundamentally a different game and why it's actually pretty fascinating technology. So, um, as some of you or most of you know like Mick partitioning is basically physical partitioning. Um, so make multi-instance GPUs um, they basically assign every partition their own fraction of actual hardware. meaning that you get proper fault isolation between jobs that are running on the same uh physical device and predictable quality of service.

Um and in general just really predictability and robustness compared to any other of the sharing solutions. Um especially in say multi-tenant environments or when bad actors might be your neighbor like consciously or not. Um Mick um MC partitioning is just the more sane technology. Um so how is it done in hardware? Uh ever
