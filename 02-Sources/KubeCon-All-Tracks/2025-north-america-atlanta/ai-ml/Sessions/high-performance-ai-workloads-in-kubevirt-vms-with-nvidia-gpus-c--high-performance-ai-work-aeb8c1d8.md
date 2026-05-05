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
speakers: ["Ezra Silvera", "IBM", "Michael Hrivnak", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27Fd3/high-performance-ai-workloads-in-kubevirt-vms-with-nvidia-gpus-challenges-and-real-world-solutions-ezra-silvera-ibm-michael-hrivnak-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=High-Performance+AI+Workloads+in+KubeVirt+VMs+With+NVIDIA+GPUs%3A+Challenges+and+Real-World+Solutions+CNCF+KubeCon+2025
slides: []
status: parsed
---

# High-Performance AI Workloads in KubeVirt VMs With NVIDIA GPUs: Challenges and Real-World Solutions - Ezra Silvera, IBM & Michael Hrivnak, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Ezra Silvera, IBM, Michael Hrivnak, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27Fd3/high-performance-ai-workloads-in-kubevirt-vms-with-nvidia-gpus-challenges-and-real-world-solutions-ezra-silvera-ibm-michael-hrivnak-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=High-Performance+AI+Workloads+in+KubeVirt+VMs+With+NVIDIA+GPUs%3A+Challenges+and+Real-World+Solutions+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre High-Performance AI Workloads in KubeVirt VMs With NVIDIA GPUs: Challenges and Real-World Solutions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fd3/high-performance-ai-workloads-in-kubevirt-vms-with-nvidia-gpus-challenges-and-real-world-solutions-ezra-silvera-ibm-michael-hrivnak-red-hat
- YouTube search: https://www.youtube.com/results?search_query=High-Performance+AI+Workloads+in+KubeVirt+VMs+With+NVIDIA+GPUs%3A+Challenges+and+Real-World+Solutions+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=USMZRseAACQ
- YouTube title: High-Performance AI Workloads in KubeVirt VMs With NVIDIA GPUs: Ch... Ezra Silvera & Michael Hrivnak
- Match score: 0.851
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/high-performance-ai-workloads-in-kubevirt-vms-with-nvidia-gpus-challen/USMZRseAACQ.txt
- Transcript chars: 24121
- Keywords: gpu, partition, nvidia, actually, create, performance, isolation, michael, switches, especially, customers, devices, everything, device, capacity, technical, talking, important

### Resumo baseado na transcript

So, one last push before the last lunch and I hope you'll enjoy this presentation. We are going to talk about how and why you can and should run high performance AI workloads in virtual machines. By the way, throughout all this presentation when I'm talking about VMs, we are talking about few use cases where one of them is that the VM is the compute node of the Kubernetes cluster. the kubert shirt if you are managing your VMs through kubernetes then you get uniform single manage agement platform to manage your containers and VMs. And this basically allows the user to use all the tools that you already know from Kubernetes, scoop cutter, cube API, CLDS, whatever you can use those to manage your VMs. Now when we are talking about virtual machines and say performance immediately people say oh the virtualization overhead.

### Excerpt da transcript

Okay. Uh, good morning everyone. I hope you had an excellent conference. That's the last day. So, one last push before the last lunch and I hope you'll enjoy this presentation. We are going to talk about how and why you can and should run high performance AI workloads in virtual machines. So, I'm Ezra Syla. I'm a senior technical staff member at IBM and with me is Michael. >> Good morning. Thank you for coming. I'm Michael Rivven, a distinguished engineer at Red Hat. Been involved one way or another with Cubevert and related things and especially putting Kubernetes on prem and at the edge for quite a number of years and very happy to see you. I'm going to turn this over to Ezra and uh and hang out down here until uh a few minutes from now. >> Okay. So, what is the plan for today? I will go through a very quick background and motivation for the work. Then present couple of key or few key technical challenges we encounter and how we solve them and also how we think this should be solved looking ahead. Then Mike will take us through real concrete customer use cases where they actually use this technology and this direction.

and we will wrap up with a short summary. So quick motivation and again Michael will walk us through some real customers use cases. So you will see the motivation there as well. But in general uh we know that when you use virtual machines you can improve flexibility. We can spin up very complex environment very quickly. It allows you also horizontal and vertical scaling quite easily. We can add GPUs to VMs. We can add VMs to clusters. By the way, throughout all this presentation when I'm talking about VMs, we are talking about few use cases where one of them is that the VM is the compute node of the Kubernetes cluster. Right? So this is why we are talking about horizontal scaling and so on. we can and enlarge the the cluster. Uh one key item and which is very important to customers is the isolation. We know that VM give better isolation and this is especially important the because it allows you to for example partition the to the specific node single node to multiple tenants right so this is very important and the last point and Michael was wearing the kubert shirt if you are managing your VMs through kubernetes then you get uniform single manage agement platform to manage your containers and VMs.

So we keep talking about VMs, VMs, VMs. Unless I'm mistaken, we are at KubeCon, right? So the missing link is the Kubet project. So let me giv
