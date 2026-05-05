---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Data Processing + Storage"
themes: ["Storage Data"]
speakers: ["Brenda McLaren", "Chris Keller", "Red Hat"]
sched_url: https://kccncna2025.sched.com/event/27FXm/untangling-csi-powering-persistent-storage-for-kubevirt-brenda-mclaren-chris-keller-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Untangling+CSI%3A+Powering+Persistent+Storage+for+KubeVirt+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Untangling CSI: Powering Persistent Storage for KubeVirt - Brenda McLaren & Chris Keller, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]]
- País/cidade: United States / Atlanta
- Speakers: Brenda McLaren, Chris Keller, Red Hat
- Schedule: https://kccncna2025.sched.com/event/27FXm/untangling-csi-powering-persistent-storage-for-kubevirt-brenda-mclaren-chris-keller-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Untangling+CSI%3A+Powering+Persistent+Storage+for+KubeVirt+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Untangling CSI: Powering Persistent Storage for KubeVirt.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXm/untangling-csi-powering-persistent-storage-for-kubevirt-brenda-mclaren-chris-keller-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Untangling+CSI%3A+Powering+Persistent+Storage+for+KubeVirt+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=m97jWRWNv0o
- YouTube title: Untangling CSI: Powering Persistent Storage for KubeVirt - Brenda McLaren & Chris Keller, Red Hat
- Match score: 0.833
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/untangling-csi-powering-persistent-storage-for-kubevirt/m97jWRWNv0o.txt
- Transcript chars: 26696
- Keywords: storage, volume, actually, driver, integration, vendor, within, drivers, virtual, handle, capabilities, controller, machines, provider, components, looking, persistent, another

### Resumo baseado na transcript

Uh so anyway, welcome to Untangling CSI, uh powering persistent storage for Cube Vert. >> Uh we're both associate principal uh solution architects at uh Red Hat and we're here to uh talk CSI. Uh so instead of every vendor reinventing the wheel and Kubernetes having to try to understand every proprietary uh system out there. CSI gives us the consistent way of managing the storage through the standard API regardless of the provider. Um, another big win is that storage is uh provisioned very dynamically. Kubernetes is going to actually look at that that definition of the of the volume that is was requested and it's going to send it to that storage provider and that storage provider is going to create that that lawn on that storage array or

### Excerpt da transcript

Uh so anyway, welcome to Untangling CSI, uh powering persistent storage for Cube Vert. Uh I'm Brendan McLaren and this is >> my name is Chris Keller. >> Uh we're both associate principal uh solution architects at uh Red Hat and we're here to uh talk CSI. So thanks for uh showing up uh to let us speak. Uh so Kubernetes made uh compute really easy right it's agile it moves from node to node it can scale uh but storage it brings complexity to the party and requires layers of abstraction uh each vendor has their own container storage interface CSI driver and of course they're all not the same and they all don't behave the same uh and then you add cube vert into the mix and you're running virtual machines on top of Kubernetes, you're just not you're not dealing with container storage anymore and it brings just a lot to um to managing that storage. Uh you have to start dealing with uh more latency issues. You have to make sure that snapshots are supported. You have to uh make sure that readrite many is supported for the live migrations to work from going from node to node.

um with your VM workloads. And so all of that's layered on top of CSI. So now you're kind of stuck in the middle of a corn field uh like just with your data waving a red flag, you know, saying here I am. Uh so what is CSI in a nutshell? Uh it's the universal translator between Kubernetes and the storage provider. And it's not going to matter who that storage provider is, right? It doesn't matter if it's uh if it's a you know a storage array that's sitting on a SAN NAS softwaredefined storage or even a cloud provider they all have that CSI driver. Uh so instead of every vendor reinventing the wheel and Kubernetes having to try to understand every proprietary uh system out there. CSI gives us the consistent way of managing the storage through the standard API regardless of the provider. Um, another big win is that storage is uh provisioned very dynamically. So when that volume is needed, that's whenever it's created. So CSI is actually the call goes to Kubernetes. Kubernetes is going to actually look at that that definition of the of the volume that is was requested and it's going to send it to that storage provider and that storage provider is going to create that that lawn on that storage array or that volume on that NAS filer or like the volume within the software defined storage.

It's going to create it on the fly and get that provision to the worker node that that workload is scheduled on
