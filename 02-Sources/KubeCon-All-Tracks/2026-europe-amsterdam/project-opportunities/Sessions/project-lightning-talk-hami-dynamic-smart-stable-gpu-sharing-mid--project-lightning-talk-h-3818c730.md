---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Mengxuan Li", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyZ/project-lightning-talk-hami-dynamic-smart-stable-gpu-sharing-middleware-in-kubernetes-mengxuan-li-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Hami%3A+Dynamic%2C+Smart%2C+Stable+GPU-Sharing+Middleware+In+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Hami: Dynamic, Smart, Stable GPU-Sharing Middleware In Kubernetes - Mengxuan Li, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Mengxuan Li, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyZ/project-lightning-talk-hami-dynamic-smart-stable-gpu-sharing-middleware-in-kubernetes-mengxuan-li-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Hami%3A+Dynamic%2C+Smart%2C+Stable+GPU-Sharing+Middleware+In+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Hami: Dynamic, Smart, Stable GPU-Sharing Middleware In Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyZ/project-lightning-talk-hami-dynamic-smart-stable-gpu-sharing-middleware-in-kubernetes-mengxuan-li-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Hami%3A+Dynamic%2C+Smart%2C+Stable+GPU-Sharing+Middleware+In+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=o96nS0o2l54
- YouTube title: Project Lightning Talk: Hami: Dynamic, Smart, Stable GPU-Sharing Middleware In Kubern... Mengxuan Li
- Match score: 1.001
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-hami-dynamic-smart-stable-gpu-sharing-middlewar/o96nS0o2l54.txt
- Transcript chars: 3767
- Keywords: gpu, resource, device, volcano, sharing, allocate, limits, memory, install, version, larger, stable, middleware, called, traditional, allocating, plugin, environment

### Resumo baseado na transcript

My name is Limousine and I'm from the Dynamia AI and I'm the maintainer of this project called Hami and the topic is smart and stable GPU sharing middleware in Kubernetes. So, if you are using the traditional way of allocating GPUs like by using a video device plugin to allocate it exclusively, you may get a very poor performance GPU cluster. And the requirements of Hami is very easy to satisfy as long as your Nvidia driver version is larger than 440 and the Kubernetes version is larger than 118. Yeah, but if you wish to use Hami DI, then your Kubernetes version need to be larger than 134. And you can just specify your GPU partitioning spec here like that you want to use two GPUs each with the memory of 10GB and 30% uh 30% of the total computing cost. Uh so, if you wish to learn more about our project, you are free to search Hami h a m i on GitHub and you can join our you can you can search our website projecthami.io.

### Excerpt da transcript

I want to make a proper introduction. My name is Limousine and I'm from the Dynamia AI and I'm the maintainer of this project called Hami and the topic is smart and stable GPU sharing middleware in Kubernetes. So, Mhm? So, if you are using the traditional way of allocating GPUs like by using a video device plugin to allocate it exclusively, you may get a very poor performance GPU cluster. And these two pictures are taken in a real production environment. You can see that the overall environment of certain GPU is about below 20% and that is it that is a very natural scenario. So, to solve this problem, we we we produce the project called Hami uh which is a GPU partitioning system and you and with it with its help, you can uh sharing the GPUs uh between multiple uh task. For example, in this mhm so in this scenario, both user A and user B can share can share their task on the on these two GPUs and leave the rest for others to use. Also, we can do that by either using traditional Hami or by using the more advanced Hami AI.

Yeah. So, I guess many of you may wonder so since we have already have a DI solution which can uh sharing GPU dynamically, so why uh Hami is about? So, mhm there are two advantage of Hami. The first one is you can allocate your GPU uh uh GPU slice by just allocating uh resource limits here. You don't need to write your resource claim which is more user-friendly, I guess. So, in this so so in this example, you wish to allocate two GPUs and each with the device memory of 10GB here. Uh and the other advantage of using Hami is we guarantee the hard resource isolation inside the container. The core component of Hami is a self-implemented uh CUDA hacking library which is injected into the container. So, you can see the output of SMI here as the upper limit of the device memory has been limited to 10GB. Yes, which which is which is done by the by by our library. Yeah. So, the method of install Hami is very easy. You just fetch your fetch the Hami repo and install it by using helm install. And then you may want to label your GPU nodes which you wish to be managed by Hami by labeling the nodes with the label GPU equals on.

And the requirements of Hami is very easy to satisfy as long as your Nvidia driver version is larger than 440 and the Kubernetes version is larger than 118. Yeah, but if you wish to use Hami DI, then your Kubernetes version need to be larger than 134. Yeah. Uh and Hami has been integrated by Volcano as well. So, if you enable th
