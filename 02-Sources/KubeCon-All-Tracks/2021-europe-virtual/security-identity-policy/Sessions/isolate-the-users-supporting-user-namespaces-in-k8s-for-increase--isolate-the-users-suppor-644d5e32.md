---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["Mauricio Vásquez", "Kinvolk"]
sched_url: https://kccnceu2021.sched.com/event/iE5B/isolate-the-users-supporting-user-namespaces-in-k8s-for-increased-security-mauricio-vasquez-kinvolk
youtube_search_url: https://www.youtube.com/results?search_query=Isolate+the+Users%21+Supporting+User+Namespaces+in+K8s+for+Increased+Security+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Isolate the Users! Supporting User Namespaces in K8s for Increased Security - Mauricio Vásquez, Kinvolk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: Virtual / Virtual
- Speakers: Mauricio Vásquez, Kinvolk
- Schedule: https://kccnceu2021.sched.com/event/iE5B/isolate-the-users-supporting-user-namespaces-in-k8s-for-increased-security-mauricio-vasquez-kinvolk
- Busca YouTube: https://www.youtube.com/results?search_query=Isolate+the+Users%21+Supporting+User+Namespaces+in+K8s+for+Increased+Security+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Isolate the Users! Supporting User Namespaces in K8s for Increased Security.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE5B/isolate-the-users-supporting-user-namespaces-in-k8s-for-increased-security-mauricio-vasquez-kinvolk
- YouTube search: https://www.youtube.com/results?search_query=Isolate+the+Users%21+Supporting+User+Namespaces+in+K8s+for+Increased+Security+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Rx-ksmLUHEY
- YouTube title: Isolate the Users! Supporting User Namespaces in K8s for Increased Security - Mauricio Vásquez
- Match score: 0.977
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/isolate-the-users-supporting-user-namespaces-in-k8s-for-increased-secu/Rx-ksmLUHEY.txt
- Transcript chars: 19022
- Keywords: username, spaces, running, support, process, mapping, cluster, container, capability, containers, coordinates, implement, inside, binary, account, isolation, network, solution

### Resumo baseado na transcript

hello everybody welcome to this presentation about supporting user namespaces in kubernetes and mauricio i work as a software engineer for kinfolk and this is my social data just in case you want to reach out in this presentation i will be explaining you what is the motivation to implement support for username spaces in kubernetes that most situation is the risk of running containers as well i will base i explain you what username spaces are and why they are important for the security of a coordinated cluster and

### Excerpt da transcript

hello everybody welcome to this presentation about supporting user namespaces in kubernetes and mauricio i work as a software engineer for kinfolk and this is my social data just in case you want to reach out in this presentation i will be explaining you what is the motivation to implement support for username spaces in kubernetes that most situation is the risk of running containers as well i will base i explain you what username spaces are and why they are important for the security of a coordinated cluster and then i will show you a bit of history and also the work that we have been doing with the community in order to implement support for user name spaces in coordinates i will also present a demo about the approval of concept that we have implemented and finally i will explain what are the next steps that we have to do in order to have this support implemented in coordinates so let's get started with the problem the main motivation of implementing username spaces in kubernetes is that running containers as root is very dangerous and when we say the a container is running normal what it means is that a process inside the container is running as root this process is able to perform privileged operations on the container and the host is usually protected by the isolation that the linus name spaces provide unfortunately this isolation is not perfect and in some cases a such a process could be able to escape the container so if our privilege process is able to escape the container this will be very bad for the host because that process will be running as a road on the horse and will be able to do a lot of damage there these are some examples of some vulnerabilities that have been found in the last year that could have been mitigated by user name spaces the last one is a special critical one because in this case an attacker is able to overwrite the run c binary in the host by just using a special container image so after that happens the attacker will have full control over the house machine as i told you these are just some examples of vulnerabilities that had been found had been found in the past and we changed uh this is very probably the in the future there are going to be more vulnerabilities and also this this this is possible that uh there are some current vulnerabilities are being exploited by the attackers let's see uh some of the mitigations that we could use in order to lower the risk of running route containers but actually the first question th
