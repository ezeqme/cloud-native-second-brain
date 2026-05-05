---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Vivek Singh", "MongoDB"]
sched_url: https://kccnceu2026.sched.com/event/2EFzv/cloud-native-theater-data-on-kubernetes-day-from-pvc-to-mount-point-dissecting-a-custom-csi-plugin-to-master-dynamic-volume-provisioning-on-kubernetes-vivek-singh-mongodb
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+From+PVC+to+Mount+Point%3A+Dissecting+a+Custom+CSI+Plugin+to+Master+Dynamic+Volume+Provisioning+on+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Data on Kubernetes Day: From PVC to Mount Point: Dissecting a Custom CSI Plugin to Master Dynamic Volume Provisioning on Kubernetes - Vivek Singh, MongoDB

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Vivek Singh, MongoDB
- Schedule: https://kccnceu2026.sched.com/event/2EFzv/cloud-native-theater-data-on-kubernetes-day-from-pvc-to-mount-point-dissecting-a-custom-csi-plugin-to-master-dynamic-volume-provisioning-on-kubernetes-vivek-singh-mongodb
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+From+PVC+to+Mount+Point%3A+Dissecting+a+Custom+CSI+Plugin+to+Master+Dynamic+Volume+Provisioning+on+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Data on Kubernetes Day: From PVC to Mount Point: Dissecting a Custom CSI Plugin to Master Dynamic Volume Provisioning on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFzv/cloud-native-theater-data-on-kubernetes-day-from-pvc-to-mount-point-dissecting-a-custom-csi-plugin-to-master-dynamic-volume-provisioning-on-kubernetes-vivek-singh-mongodb
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Data+on+Kubernetes+Day%3A+From+PVC+to+Mount+Point%3A+Dissecting+a+Custom+CSI+Plugin+to+Master+Dynamic+Volume+Provisioning+on+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MY-VaJVJmk0
- YouTube title: Cloud Native Theater | Data on Kubernetes Day: From PVC to Mount Point: Dissecting a... Vivek Singh
- Match score: 0.799
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-data-on-kubernetes-day-from-pvc-to-mount-point-di/MY-VaJVJmk0.txt
- Transcript chars: 16291
- Keywords: volume, plug-in, resource, provisioner, particular, controller, actually, exactly, create, storage, called, sidecar, attachment, created, attached, component, provider, annotation

### Resumo baseado na transcript

I am a software engineer at MongoDB and in this particular session we are going to look into how exactly dynamic volume provisioning happens in case of Kubernetes. So in case of Kubernetes uh when you try to let's say if you have a use case where uh when you want to run a stateful work workload on top of Kubernetes you would want to have a volume attached to that workload and so that if something goes wrong we would be able to let's say debug that problem we would be able to understand the issues. So like I said uh in case of Kubernetes we we have a very nice API very nice resource called PVC persistent volume claim and as soon as you create a persistent volume claim resource with a specific requirement let's say you want maybe uh 50 GB of of a volume uh in that case you create the PVC resource and as soon as the PVC resource is created the persistent volume controller that is shipped with Kubernetes controller manager that looks into that PBC resource and then it basically So we have a PVC PVC refers to a storage class resource where the provisioner is actually specified and the provisioner name for a for a particular volume uh can either have kubernetes.io in in the name or not.

### Excerpt da transcript

All right. Uh hey hello everyone. Uh my name is Vivee. I am a software engineer at MongoDB and in this particular session we are going to look into how exactly dynamic volume provisioning happens in case of Kubernetes. So in case of Kubernetes uh when you try to let's say if you have a use case where uh when you want to run a stateful work workload on top of Kubernetes you would want to have a volume attached to that workload and in that case Kubernetes gives us a powerful API it's it's PVC API and the problem with PVC API is as soon as you create a PVC resource First a volume magically appears and gets attached to your Kubernetes node that can later be attached to the pod so that your pod can consume that volume. And that magic word that I used that's the problem in in today's world I would say. So I was I was talking to some some guys uh day before yesterday uh while dinner and it looks like a lot of platform teams are still not very confident in running their stateful workloads on Kubernetes.

So that's exactly what this session is going to focus on. this particular session in this particular session we are going to talk about the entire workflow entire journey of a of a PVC resource uh from when you when you create the PVC resource how exactly it's provisioned how exactly it's attached to the to the node and then later to your pod and understanding that behind the scene mechanism is at least according to me very very crucial in running your stateful workloads on on Kubernetes if you don't understand how exactly that storage layer works. You will not really be confident in your running uh stateful stateful applications on on top of Kubernetes and after after this session I think we are going to going to go away with the kind of enough understanding about about the dynamic volume provisioning so that if something goes wrong we would be able to let's say debug that problem we would be able to understand the issues. So like I said uh in case of Kubernetes we we have a very nice API very nice resource called PVC persistent volume claim and as soon as you create a persistent volume claim resource with a specific requirement let's say you want maybe uh 50 GB of of a volume uh in that case you create the PVC resource and as soon as the PVC resource is created the persistent volume controller that is shipped with Kubernetes controller manager that looks into that PBC resource and then it basically figures out if there are there are any already available volumes
