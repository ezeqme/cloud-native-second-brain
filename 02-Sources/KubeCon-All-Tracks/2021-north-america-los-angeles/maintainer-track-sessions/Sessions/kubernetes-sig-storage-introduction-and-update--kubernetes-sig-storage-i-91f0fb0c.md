---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Xing Yang", "VMware", "Michelle Au", "Google"]
sched_url: https://kccncna2021.sched.com/event/lV8L/kubernetes-sig-storage-introduction-and-update-xing-yang-vmware-michelle-au-google
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+SIG+Storage+Introduction+and+Update+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Kubernetes SIG Storage Introduction and Update - Xing Yang, VMware & Michelle Au, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Xing Yang, VMware, Michelle Au, Google
- Schedule: https://kccncna2021.sched.com/event/lV8L/kubernetes-sig-storage-introduction-and-update-xing-yang-vmware-michelle-au-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+SIG+Storage+Introduction+and+Update+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Kubernetes SIG Storage Introduction and Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV8L/kubernetes-sig-storage-introduction-and-update-xing-yang-vmware-michelle-au-google
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+SIG+Storage+Introduction+and+Update+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-r8t24qVvUA
- YouTube title: Kubernetes SIG Storage Introduction and Update - Xing Yang, VMware & Michelle Au, Google
- Match score: 0.799
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/kubernetes-sig-storage-introduction-and-update/-r8t24qVvUA.txt
- Transcript chars: 21904
- Keywords: volume, storage, driver, feature, volumes, drivers, migration, provisioning, support, features, cluster, windows, containers, specific, write, container, plugins, called

### Resumo baseado na transcript

hello everyone today michelle and i will give an introduction and update to kubernetes seek storage my name is xin yang i work at a vmware in the cloud 30 team i'm also a co-chair in six storage along with sadali from google hi i'm michelle i'm a tech lead for six storage and then um also uh yawn from red hat is another tech lead in six storage so our session today will include two parts in the first half we will give an introduction in the second half your volumes have a lot of data inside of them the next fs group related feature is called csifs group policy this feature allows a csi driver to explicitly opt into supporting fs group previously without this kubernetes uses a heuristic to determine which drivers

### Excerpt da transcript

hello everyone today michelle and i will give an introduction and update to kubernetes seek storage my name is xin yang i work at a vmware in the cloud 30 team i'm also a co-chair in six storage along with sadali from google hi i'm michelle i'm a tech lead for six storage and then um also uh yawn from red hat is another tech lead in six storage so our session today will include two parts in the first half we will give an introduction in the second half we will give an update and deep dive in the introduction i'm going to talk about some basic concepts in kubernetes storage and how to get involved first i'll talk about persistent storage kubernetes storage provides a way for containers in the pods to consume block or file storage persistent storage is one type of storage that leaves beyond a pod's life cycle the terminologies we heard most in six storage are probably pvc pv and storage class pvc persistent volume claim is a user space object it is a request by a user for storage a pv persistent volume is the cluster scope object it represents a physical volume on the storage system a pvc and a pv have a one-on-one mapping storage class is in the cluster scope it is a way for admin to describe the classes of storage different classes might map to different quality of service levels or other admin defined policies in dynamic provisioning study class is used to find out which provisional should be used and what parameters should be passed to the provisioner when creating the volume a pod is a group of one or more containers with shared storage and network resources and a specification for how to run the containers a pod is a user space object a pvc is used by a pod in static provisioning a cluster admin creates a number of pvs which carry the details of the real storage the control plane can bind the pvcs to pvs in cluster however if you want a pvc to bind to a specific specific pv you need to pre-bind them when none of the static pvs the admin created match a user's pvc the cluster may try to dynamically provision a volume especially for the pvc this provisioning is based on study classes the pvc must request a story class and the admin must have created and configured that class for dynamic provisioning to occur here is an example of a pod pvc and the story class the pod is using the pvc pvc has capacity access modes it is a rewrite once here and storage class name specified here in the studio class there is a provisioner that determines what volume plugin i
