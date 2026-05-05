---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Xing Yang", "Co-chair SIG Storage"]
sched_url: https://kccnceu2025.sched.com/event/1tcw0/project-lightning-talk-whats-new-in-kubernetes-storage-xing-yang-co-chair-sig-storage
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+Kubernetes+Storage+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: What's New in Kubernetes Storage - Xing Yang, Co-chair SIG Storage

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Xing Yang, Co-chair SIG Storage
- Schedule: https://kccnceu2025.sched.com/event/1tcw0/project-lightning-talk-whats-new-in-kubernetes-storage-xing-yang-co-chair-sig-storage
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+Kubernetes+Storage+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: What's New in Kubernetes Storage.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcw0/project-lightning-talk-whats-new-in-kubernetes-storage-xing-yang-co-chair-sig-storage
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+What%27s+New+in+Kubernetes+Storage+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JhMwxRfi7Ho
- YouTube title: Project Lightning Talk: What's New In Kubernetes Storage - Xing Yang
- Match score: 0.995
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-whats-new-in-kubernetes-storage/JhMwxRfi7Ho.txt
- Transcript chars: 3397
- Keywords: volume, storage, release, parameters, provisioned, attribute, highlight, expand, feature, attributes, sidecars, lightning, recover, resize, failure, entering, finally, specify

### Resumo baseado na transcript

One expansion has been around for a while, but without the ability to recover from resize failure, you could get stuck while trying to expand your volume. Let's say you try to expand your volume from one terabyte to 10 terabytes. When you provision PVC, you can uh specify a storage class name in your PVC. CSI sidecars are helper containers that watch Kubernetes API objects and trigger volume operations against a CSI driver. So with all the side cars that means after every Kubernetes release we will need to release all the side cars and also resource utilization is a concern. To solve all these problems we want to consolidate all the side cars into one mono repo.

### Excerpt da transcript

Welcome to the project lightning talk for six storage. My name is Shing Yang. I work for VMwell by Broadcom. In six storage, Sad and myself are co-chairs. Michelle and I are tech leads. Other than the leads, there are also many other contributors. We have been working on a number of very exciting projects. Let me highlight a few. The first project I want to highlight is recover from resize failure. One expansion has been around for a while, but without the ability to recover from resize failure, you could get stuck while trying to expand your volume. Let's say you try to expand your volume from one terabyte to 10 terabytes. Instead of entering 10, you entered 100 by accident. you don't really have that much capacity in your storage system to complete this extension. Kubernetes will keep retrying but it will never be successful. This problem turned out to be hard to solve because we never intended to support the shrinking of volumes. So, uh it took us quite a while to figure out how to fix this problem.

um we basically um let's say come to this uh side we fix it and this feature is finally GA in Kubernetes 1.34 release. Um so with this fix you can simply fix your problem by entering a new PVC size. So the new size still has to be larger than the original size of your volume. And like in this example, you can just enter 10 and it will finally expand it to your desired size. The next feature I want to highlight is volume attributes class. When you provision PVC, you can uh specify a storage class name in your PVC. And this search class defines parameters to be used for dynamic provisioning after the volume is provisioned. However, you cannot change those parameters. Um so there are use cases where require the volume options such as I ops for or throughput to be modified after volume is provisioned. That's why we introduced volume attributes class. So with volume after class we can also define parameters for dynamic provisioning and after the volume is provisioned you can modify those parameters. So here we have two volume attributes classes silver and gold and in the PVC spec you specify the volume attribute class name.

Although the search class name is still immutable, the volume attribute volume attribute class name is mutable. After the volume is provisioned, you can change your volume attribute class name from silver to gold. That will trigger the volume to be modified to have the new IOPS as defined in the volume attri class gold. This feature is now G
