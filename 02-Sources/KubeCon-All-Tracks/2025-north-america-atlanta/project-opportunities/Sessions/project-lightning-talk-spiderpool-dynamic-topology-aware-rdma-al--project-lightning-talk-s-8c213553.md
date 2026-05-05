---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML"]
speakers: ["Weizhou Lan", "Technical Lead"]
sched_url: https://kccncna2025.sched.com/event/27d4N/project-lightning-talk-spiderpool-dynamic-topology-aware-rdma-allocation-for-gpu-based-ai-workloads-weizhou-lan-technical-lead
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Spiderpool%3A+Dynamic+Topology-Aware+RDMA+Allocation+For+GPU-Based+AI+Workloads+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Spiderpool: Dynamic Topology-Aware RDMA Allocation For GPU-Based AI Workloads - Weizhou Lan, Technical Lead

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]]
- País/cidade: United States / Atlanta
- Speakers: Weizhou Lan, Technical Lead
- Schedule: https://kccncna2025.sched.com/event/27d4N/project-lightning-talk-spiderpool-dynamic-topology-aware-rdma-allocation-for-gpu-based-ai-workloads-weizhou-lan-technical-lead
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Spiderpool%3A+Dynamic+Topology-Aware+RDMA+Allocation+For+GPU-Based+AI+Workloads+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Spiderpool: Dynamic Topology-Aware RDMA Allocation For GPU-Based AI Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4N/project-lightning-talk-spiderpool-dynamic-topology-aware-rdma-allocation-for-gpu-based-ai-workloads-weizhou-lan-technical-lead
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Spiderpool%3A+Dynamic+Topology-Aware+RDMA+Allocation+For+GPU-Based+AI+Workloads+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fBE6UiLROWA
- YouTube title: Project Lightning Talk: Spiderpool: Dynamic Topology-Aware RDMA Allocation For GPU... Weizhou Lan
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-spiderpool-dynamic-topology-aware-rdma-allocati/fBE6UiLROWA.txt
- Transcript chars: 2800
- Keywords: gpu, allocation, resource, device, inference, plug-in, affinity, containers, network, dynamic, workloads, topology, cluster, parallel, assign, dedicated, traffic, networking

### Resumo baseado na transcript

Today I will be talking about sparo dynamic topology aware RDMA allocation for GPU based AI workloads in a multi- tenant inference cluster we need to use every bit of GPU resource efficiently. Suppose there are multiple distributed inference task that use tensor par parallel uh with four GPUs per node and data parallel across two parts on two nodes. This slide demonstrates one approach provided by Spiple called uh prefind resource allocation. This slide demonstrate another approach called adapt adaptive RDM resource allocation.

### Excerpt da transcript

Hi everyone, thank you for joining. Today I will be talking about sparo dynamic topology aware RDMA allocation for GPU based AI workloads in a multi- tenant inference cluster we need to use every bit of GPU resource efficiently. Suppose there are multiple distributed inference task that use tensor par parallel uh with four GPUs per node and data parallel across two parts on two nodes. In that case GPU and RDMA uh device allocation on each node must be very fine grind in a cluster where to meet these uh needs. We must solve two key issues. First, I think the device plug-in for GPU and RDMA are separate components. When just allocating a subset of GPU on each node, they don't they don't uh coordinate the allocation of GPU and RDMA device resource based on PCIe uh uh affinity for the GDR. Uh second we need to assign uh each port a set of dedicated RDMA device uh each with its own IP address uh so that RDMA traffic can be identified and observed. Spot is a singi project singi plug-in that uh provides for singi functionality.

It enables underlay networking for containers particularly uh for uh RDMA network interface. Uh in its latest version uh it implements DIA and NI uh capability allowing it to better meet the networking requirements of AI inference. As mentioned in previous slide, it can detect the PCIe affinity between n and GPUs and provide fine grain allocation of RDMA devices. On the other hand, based on SIOV containers can be provided with dedicated RD minix and independent IP addresses uh ensuring that each containers RDM traffic can uh is individually uh traceable within the network. So let let's dive into the details. This slide demonstrates one approach provided by Spiple called uh prefind resource allocation. In advance, a resource claim template can be created to how interfaces should be assigned from a set of master network interfaces. When creating a port uh users can reference this uh resource claim and the spy port will then apply only the specifi uh specified adminix to the port uh without considering PCIe uh topology for GPU.

Through this usage pattern uh administrators uh can have fine grain fine grand control over how RDMA devices are allocated. This slide demonstrate another approach called adapt adaptive RDM resource allocation. Users are not required to spiceify detailed configurations during the NI phase of port start up on a node. Sparot detects the PCIe slot of GPU uh allocated by the GPU device plugin and the and then adaptively
