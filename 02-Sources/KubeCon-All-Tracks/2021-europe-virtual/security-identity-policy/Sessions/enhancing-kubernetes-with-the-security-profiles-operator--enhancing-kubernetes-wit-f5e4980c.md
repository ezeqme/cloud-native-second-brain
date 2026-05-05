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
themes: ["Observability", "Security", "Kubernetes Core"]
speakers: ["Colleen Murphy", "Sascha Grunert", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/iE3C/enhancing-kubernetes-with-the-security-profiles-operator-colleen-murphy-sascha-grunert-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Enhancing+Kubernetes+with+the+Security+Profiles+Operator+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Enhancing Kubernetes with the Security Profiles Operator - Colleen Murphy & Sascha Grunert, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Observability]], [[Security]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Colleen Murphy, Sascha Grunert, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/iE3C/enhancing-kubernetes-with-the-security-profiles-operator-colleen-murphy-sascha-grunert-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Enhancing+Kubernetes+with+the+Security+Profiles+Operator+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Enhancing Kubernetes with the Security Profiles Operator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3C/enhancing-kubernetes-with-the-security-profiles-operator-colleen-murphy-sascha-grunert-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Enhancing+Kubernetes+with+the+Security+Profiles+Operator+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xisAIB3kOJo
- YouTube title: Enhancing Kubernetes with the Security Profiles Operator - Colleen Murphy & Sascha Grunert, Red Hat
- Match score: 0.827
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/enhancing-kubernetes-with-the-security-profiles-operator/xisAIB3kOJo.txt
- Transcript chars: 22084
- Keywords: profile, profiles, seccomp, security, operator, create, resource, cluster, application, recording, selinux, workload, deployment, workloads, context, feature, container, actually

### Resumo baseado na transcript

Hello, and welcome to our presentation on enhancing Kubernetes with a security profiles operator. I'm a contributor to the security profiles operator, and I'm a software engineer at SUSE, and it's a pleasure to be here with you today. So, this means that Kubernetes has to be designed for usability over security. Other than that, security-related decisions have to be considered by the system administrators, the site reliability engineers, as well as application developers. The security context of Kubernetes holds the security configuration that will be applied to a pod or a container. So, this native API field makes the usage of the security feature more comfortable, because the API server can validate the fields directly while applying them to the workload.

### Excerpt da transcript

Hello, and welcome to our presentation on enhancing Kubernetes with a security profiles operator. My name's Colleen. I'm a contributor to the security profiles operator, and I'm a software engineer at SUSE, and it's a pleasure to be here with you today. Hey friends, I'm Sasha, one of the maintainers of the security profiles operator, and it's a pleasure to be here today. And I work for Red Hat. What will we cover in this talk? Well, first of all, we would like to speak about how to enhance default Kubernetes workload security. So, we would like to speak about which goals we would have in mind, and how to achieve that in such a rapidly evolving project like Kubernetes. Secondly, we would like to lay out the current state of the security profiles operator. So, we will cover the operator features in detail, and how they can be used to make workloads more secure. And then, we will see the operator in action. So, this is time for demoing the operator while keeping common use cases in mind. And after that, last but not least, we will lay out our plan for the future of the project.

So, for example, we will discuss our long-term goals, and we'll leave some room for some Q&A session afterwards. How to enhance default workload security in Kubernetes? Kubernetes does not provide strong security defaults out of the box. So, this means that Kubernetes has to be designed for usability over security. So, for example, if we decide to restrict the syscalls of a workload, then we can keep have to keep in mind that this may break applications while it makes others more secure. Other than that, security-related decisions have to be considered by the system administrators, the site reliability engineers, as well as application developers. And those different roles make it hard for the community project to decide which position may be the most important one, and which should be considered as the default. The security context of Kubernetes holds the security configuration that will be applied to a pod or a container. So, this native API field makes the usage of the security feature more comfortable, because the API server can validate the fields directly while applying them to the workload.

Some security-related features like AppArmor are not graduated to the security context yet. They are still using the annotation-based syntax to apply settings to workloads, which is not obvious to use, and which is kind of error-prone because containers have to reference have to be referenc
