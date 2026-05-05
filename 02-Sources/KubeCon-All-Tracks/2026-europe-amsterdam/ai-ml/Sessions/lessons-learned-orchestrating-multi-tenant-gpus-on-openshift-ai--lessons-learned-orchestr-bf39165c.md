---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Luca Berton", "Dell Technologies"]
sched_url: https://kccnceu2026.sched.com/event/2CVzs/lessons-learned-orchestrating-multi-tenant-gpus-on-openshift-ai-with-nvidia-kai-gh200-luca-berton-dell-technologies
youtube_search_url: https://www.youtube.com/results?search_query=Lessons+Learned+Orchestrating+Multi-Tenant+GPUs+on+OpenShift+AI+with+NVIDIA+KAI+%28G%2FH200%29+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Lessons Learned Orchestrating Multi-Tenant GPUs on OpenShift AI with NVIDIA KAI (G/H200) - Luca Berton, Dell Technologies

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Luca Berton, Dell Technologies
- Schedule: https://kccnceu2026.sched.com/event/2CVzs/lessons-learned-orchestrating-multi-tenant-gpus-on-openshift-ai-with-nvidia-kai-gh200-luca-berton-dell-technologies
- Busca YouTube: https://www.youtube.com/results?search_query=Lessons+Learned+Orchestrating+Multi-Tenant+GPUs+on+OpenShift+AI+with+NVIDIA+KAI+%28G%2FH200%29+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Lessons Learned Orchestrating Multi-Tenant GPUs on OpenShift AI with NVIDIA KAI (G/H200).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzs/lessons-learned-orchestrating-multi-tenant-gpus-on-openshift-ai-with-nvidia-kai-gh200-luca-berton-dell-technologies
- YouTube search: https://www.youtube.com/results?search_query=Lessons+Learned+Orchestrating+Multi-Tenant+GPUs+on+OpenShift+AI+with+NVIDIA+KAI+%28G%2FH200%29+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nABVTFBmV2M
- YouTube title: Lessons Learned Orchestrating Multi-Tenant GPUs on OpenShift AI with NVIDIA KAI (G/H2... Luca Berton
- Match score: 1.003
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/lessons-learned-orchestrating-multi-tenant-gpus-on-openshift-ai-with-n/nABVTFBmV2M.txt
- Transcript chars: 14974
- Keywords: gpu, platform, openshift, network, nvidia, another, become, tenant, customer, environment, cluster, component, important, driver, visibility, access, persona, argo

### Resumo baseado na transcript

Today I want to share a practical blueprint of running multi-tenant GPUs on bare metal OpenShift AI delivering a sovereign full-stack AI platform that drives immediate result. The hard part is sharing them safely, fairly, and efficiently across teams. Uh What we learned at very quickly that a working GPU cluster is not the same as a shareable GPU platform. Driver drift is also another problem, especially because this doesn't allow a core here visibility across the cluster. The challenge become how do we prevent chaos before tenants ever feel it? The tenant admin tenant admin wants boundaries and visibility into cost.

### Excerpt da transcript

Welcome everybody. Today I want to share a practical blueprint of running multi-tenant GPUs on bare metal OpenShift AI delivering a sovereign full-stack AI platform that drives immediate result. The key point is this. Getting GPUs to run is not the hard part. The hard part is sharing them safely, fairly, and efficiently across teams. My name is Luca Berton. I work on AI-ready infrastructure and enterprise cloud environments at Dell Consulting. And these tools come from hands-on practical platform work delivering to an avionics customer in France in production today. What I will show you is the result of operational lessons from real systems. You're here for the architectural overview. And this is based on the Dell AI factory. This was a bare metal environment layered on Red Hat Kubernetes OpenShift. OpenShift AI will then capsule all the best project that drive AI innovation. Oh, I forgot to tell you. All the slide are available throughout this QR code, but I will show you also at the end of the presentation.

Where was I? Okay. OpenShift AI is the component that encapsulate all the open source project related to AI. But other two components are very important. Nvidia GPU and network operator, and as well having good GPUs. In this for this customer we use a Grasshopper H200 GPU nodes with more than 137 gigabyte each. And we're leveraging the latest Dell AI server that can manage up to eight GPU card per node. Uh Another challenge was RDMA for storage. And another small thing, this is air-gapped setup with local mirrors. In the cloud some complexity is abstracted away. Here every layer is our to own, configure, and recover. In total we installed more than 2 TB of data downloading all the intricacy of dependency between all the various component. Uh What we learned at very quickly that a working GPU cluster is not the same as a shareable GPU platform. The real risk were noisy neighbor, queue starvation, mismatched MIG behavior. Enough familiar with MIG is a way of slicing GPU in predefined way, like a half, quarter, and so on and so forth.

You can divide by the tensor core or the GPU memory. And there are some already provided profile. Driver drift is also another problem, especially because this doesn't allow a core here visibility across the cluster. Um Networking failures around SR-IOV and RDMA, I would say that were the most interesting thing part of the project that require a little bit of more love. The challenge become how do we prevent chaos before
