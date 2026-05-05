---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security"]
speakers: ["Tsuzuki Tsuchiya", "Kento Kubo", "LY Corporation"]
sched_url: https://kccnceu2026.sched.com/event/2CW42/exploring-nri-for-automated-ca-trust-injection-tsuzuki-tsuchiya-kento-kubo-ly-corporation
youtube_search_url: https://www.youtube.com/results?search_query=Exploring+NRI+for+Automated+CA+Trust+Injection+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Exploring NRI for Automated CA Trust Injection - Tsuzuki Tsuchiya & Kento Kubo, LY Corporation

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Tsuzuki Tsuchiya, Kento Kubo, LY Corporation
- Schedule: https://kccnceu2026.sched.com/event/2CW42/exploring-nri-for-automated-ca-trust-injection-tsuzuki-tsuchiya-kento-kubo-ly-corporation
- Busca YouTube: https://www.youtube.com/results?search_query=Exploring+NRI+for+Automated+CA+Trust+Injection+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Exploring NRI for Automated CA Trust Injection.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW42/exploring-nri-for-automated-ca-trust-injection-tsuzuki-tsuchiya-kento-kubo-ly-corporation
- YouTube search: https://www.youtube.com/results?search_query=Exploring+NRI+for+Automated+CA+Trust+Injection+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6qvsce4t2_w
- YouTube title: Exploring NRI for Automated CA Trust Injection - Tsuzuki Tsuchiya & Kento Kubo, LY Corporation
- Match score: 0.761
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/exploring-nri-for-automated-ca-trust-injection/6qvsce4t2_w.txt
- Transcript chars: 15630
- Keywords: container, certificates, private, approach, containers, create, injection, server, bundle, environment, cluster, plugin, support, internal, command, certificate, nodejs, runtimes

### Resumo baseado na transcript

Today we are going to talk about NRI N resource interface and how it can help us to automate an operational toy by showing a case that automates uh the SI trust injection. First, let me explain our private crowd and private CA to share the context. PKI is one of the fundamental technologies for their trust architecture. With a private CA we can enforce security policies and enable mutual TRS with asends and issue server certificates for the internal services. But installing the private CS certificates everywhere isn't simple uh at the scale of our crowd and when especially using containers. Cluster trust bundle is a kubernetes standard uh cluster scoped object to store and distribute CS certificates in the cluster.

### Excerpt da transcript

Thank you for joining us today. Uh I'm Tuzukit. Today we are going to talk about NRI N resource interface and how it can help us to automate an operational toy by showing a case that automates uh the SI trust injection. My name is Suzuit from Corporation in Japan. I'm I work on the development and operation of internal platforms. My name is Kent Kubo, a software engineer at LY Corporation. I'm also a developer of internal command platform. Uh these are these are today's topics. First, let me explain our private crowd and private CA to share the context. Next, I describe the challenges to inject SH certificates into containers. I also describe uh existing approaches and their problems here. Then I introduce NRI node resource interface and our solution with NRI. Lastly I compare it with existing ones. Uh first let me explain our private cloud. Our private cloud is running on multiple on premises data centers. It uses OpenStack for managing VMs and uses Ascend for IM identity access management. Ascend is a CNCF sandbox project for service to service authentication and authorization with ARB.

And we are part of Kubernetes as a service team to provide a single tenant Kubernetes Kubernetes clusters to internal developers. We operate more than 1,000 kubernetes clusters powered by cluster API and security is also important to also important to us. We have the internal PKI to manage the private CA for the flexible certificate management. PKI is one of the fundamental technologies for their trust architecture. With a private CA we can enforce security policies and enable mutual TRS with asends and issue server certificates for the internal services. It means not exposed to the internet. So external users cannot trust the certificates signed by the private CA but internal users can internal users in my company can trust them because the private CA certificates are installed in our laptops and servers. But installing the private CS certificates everywhere isn't simple uh at the scale of our crowd and when especially using containers. I think everyone here has run into this kind of error that the client cannot trust trust the server.

This is caused because uh the CS certificates aren't installed in your images. So if you want to install the public CS certificates, you can install them from the public package manager like uh after get install CS certificates command. But if you want to install the private CS certificates, you need some tricks. Let me let me explain th
