---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Alice Frosi", "Red Hat"]
sched_url: https://kccnceu2022.sched.com/event/ytu1/its-all-for-the-users-more-durable-secure-and-pluggable-kubevirt-v053-alice-frosi-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=It%E2%80%99s+All+for+the+Users.+More+Durable%2C+Secure%2C+and+Pluggable.+KubeVirt+v0.53+CNCF+KubeCon+2022
slides: []
status: parsed
---

# It’s All for the Users. More Durable, Secure, and Pluggable. KubeVirt v0.53 - Alice Frosi, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Alice Frosi, Red Hat
- Schedule: https://kccnceu2022.sched.com/event/ytu1/its-all-for-the-users-more-durable-secure-and-pluggable-kubevirt-v053-alice-frosi-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=It%E2%80%99s+All+for+the+Users.+More+Durable%2C+Secure%2C+and+Pluggable.+KubeVirt+v0.53+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre It’s All for the Users. More Durable, Secure, and Pluggable. KubeVirt v0.53.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytu1/its-all-for-the-users-more-durable-secure-and-pluggable-kubevirt-v053-alice-frosi-red-hat
- YouTube search: https://www.youtube.com/results?search_query=It%E2%80%99s+All+for+the+Users.+More+Durable%2C+Secure%2C+and+Pluggable.+KubeVirt+v0.53+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=L9H0pz5PpKo
- YouTube title: It’s All for the Users. More Durable, Secure, and Pluggable. KubeVirt v0.53 - Alice Frosi, Red Hat
- Match score: 0.955
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/its-all-for-the-users-more-durable-secure-and-pluggable-kubevirt-v0-53/L9H0pz5PpKo.txt
- Transcript chars: 23040
- Keywords: cluster, virtual, basically, already, running, machine, control, create, inside, support, access, storage, machines, command, course, volume, kubert, snapshot

### Resumo baseado na transcript

everyone i think it's time to start so let's introduce myself my name is alicia froze i'm from reddit and today i'm going to tell you what happened in the past years in hubert so first of all this is not going to be an introduction about kubert if you have the chance to attend our virtual office hours you get already an introduction but if you are completely new to keyword you can think about hubert as a kubernetes extension so designed to be kubernetes native in order to

### Excerpt da transcript

everyone i think it's time to start so let's introduce myself my name is alicia froze i'm from reddit and today i'm going to tell you what happened in the past years in hubert so first of all this is not going to be an introduction about kubert if you have the chance to attend our virtual office hours you get already an introduction but if you are completely new to keyword you can think about hubert as a kubernetes extension so designed to be kubernetes native in order to run virtual machines using livert and kvm inside containers so in cuber we focus on many different areas we add new virtualization feature we focus on improvement of security but also we try to be part of the kubernetes ecosystem so we integrate with various projects in order to offer a more robust and scalable platform so cubert recently has been graduated as cnc avetine project and this shows how you can effectively be around virtual machine using kubernetes so one of the strongest use cases for kubernetes running gpu's workload and usually this cannot be effectively run with the regular containers one example is the slicing of a cp of a physical gpus so with cuber you can create us and slice partitioning gpus using mediated devices and then you can assign those virtual devices to different vms for example so initially the creation of these devices needed to be done manually in kubert and recently we added the automation and the cuber will automatically create immediate devices based on the configuration so this has been one of the recent improvements that we did in this area usually to run [Music] virtual machine effectively we need to pass very low level information to the pod where the vm is running an example is cpu topology and in this direction we had recently the new affinity for the assigned device to the virtual machines this for example is particularly useful if the vm is using sriv devices or again gpus so one of the goal of keyword is to abstract the workload definition from the different options in order to tune your vms one example is the real-time workload so as a user you just simply need to specify that you want to run real-time workload that will be just an option on the declaration of your vms and then cuber basically automatically pick the best revert option but it also schedules the vm on a node with the kernel real-time support so we focus on different areas storage is one of those and in storage area we have we did a lot of improvement but we also integrated with
