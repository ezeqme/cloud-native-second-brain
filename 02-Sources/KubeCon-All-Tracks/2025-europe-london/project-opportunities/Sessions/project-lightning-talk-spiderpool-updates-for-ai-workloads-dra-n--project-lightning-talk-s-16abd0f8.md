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
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Weizhou Lan", "Maintainer and Technical Lead"]
sched_url: https://kccnceu2025.sched.com/event/1tcuh/project-lightning-talk-spiderpool-updates-for-ai-workloads-dra-nri-and-rdma-observability-weizhou-lan-maintainer-and-technical-lead
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Spiderpool+Updates+For+AI+Workloads%3A+DRA%2C+NRI%2C+and+RDMA+Observability+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Spiderpool Updates For AI Workloads: DRA, NRI, and RDMA Observability - Weizhou Lan, Maintainer and Technical Lead

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Weizhou Lan, Maintainer and Technical Lead
- Schedule: https://kccnceu2025.sched.com/event/1tcuh/project-lightning-talk-spiderpool-updates-for-ai-workloads-dra-nri-and-rdma-observability-weizhou-lan-maintainer-and-technical-lead
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Spiderpool+Updates+For+AI+Workloads%3A+DRA%2C+NRI%2C+and+RDMA+Observability+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Spiderpool Updates For AI Workloads: DRA, NRI, and RDMA Observability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcuh/project-lightning-talk-spiderpool-updates-for-ai-workloads-dra-nri-and-rdma-observability-weizhou-lan-maintainer-and-technical-lead
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Spiderpool+Updates+For+AI+Workloads%3A+DRA%2C+NRI%2C+and+RDMA+Observability+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Cx5c-IueP78
- YouTube title: Project Lightning Talk: Spiderpool Updates For AI Workloads: DRA, NRI, and RDMA Obser... Weizhou Lan
- Match score: 0.981
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-spiderpool-updates-for-ai-workloads-dra-nri-and/Cx5c-IueP78.txt
- Transcript chars: 2993
- Keywords: network, resource, scheduling, solution, allocate, multi-tenant, devices, number, affinity, updates, observability, latest, supports, provides, challenges, configuration, necessary, perfect

### Resumo baseado na transcript

Uh I'm Wizo L from dolot and today I'm here to share the latest updates on the s project spar. uh spo is an all-in-one Singi solution and it can be used as independent Singi with uh rich futures and it could allocate secondary network cards uh in conjunction with other SI and the spo perfectly supports uh RDMA network uh for AI jobs uh Therefore in order to support multi-tenant scenarios with MAC van or SOV spot supports outputting RDM metrics for all namespace on the node by associating the labels of port name.

### Excerpt da transcript

Hi everyone. Sorry for the delay only to my laptop. Okay. Uh I'm Wizo L from dolot and today I'm here to share the latest updates on the s project spar. uh spo is an all-in-one Singi solution and it can be used as independent Singi with uh rich futures and it could allocate secondary network cards uh in conjunction with other SI and the spo perfectly supports uh RDMA network uh for AI jobs uh especially in multi-tenant uh it provides complimentary uh features such as RDMA uh observability and right limiting. Uh in past practices we encounted uh several challenges. Uh on one hand the singi annotation configuration is to be written in the yamo when using RDMA devices. It is uh necessary to manually uh query and uh uh configure the it uh the RDM resource name for each network which is uh terrible uh use experience. uh on on the other hand the underlying network of each host is complex and a perfect a perfect network solution uh scheduling solution for ports uh uh are not found. So this networking scheduling requirements span uh m multiple dimensions.

So uh in the latest uh we aim to address these challenges using DIA uh spo DIA implementation could uh completely finish the allocation of network interfaces based on divers diversified strategies in resource size objects uh status for network interface is continually reported. It includes kinds of uh interface information uh even such as PCI or find the GPUs uh RDMA network region. Uh therefore it could help achieve uh future range network scheduling strategies with the selector in the resource claim object. uh in the DIA implementation of sparo uh pot can use the resource claim to associate the CI configuration. Uh the expected number of network interfaces is clearly specified in the uh resource claim object. Uh additionally uh spec specific scheduling requirements can be implemented using the selectors in the resource claim. uh in multi-tenant environments with Mac villain or ISO we can uh consider an interesting need uh particularly when ports require fewer than eight GPUs it is only necessary to allocate an equal number of RDMA devices to the port with GDR affinity this is uh there's no way to achieve that with traditional methods To address this, we developed a future of called uh dynamic uh assignment.

In resource claim, only a request for a device class named the GPU affinity needs to be declared during the NI phase of port start up. Uh SP detect the assigned GPUs and uh allocate RDM with GDI affinity o
