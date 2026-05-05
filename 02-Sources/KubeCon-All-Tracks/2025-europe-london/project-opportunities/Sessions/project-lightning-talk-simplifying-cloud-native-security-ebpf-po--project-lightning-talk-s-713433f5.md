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
themes: ["AI ML", "Security", "Networking", "Community Governance"]
speakers: ["Muyang Tian", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcvl/project-lightning-talk-simplifying-cloud-native-security-ebpf-powered-encryption-in-sidecarless-service-mesh-muyang-tian-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Simplifying+Cloud-Native+Security%3A+eBPF-Powered+Encryption+in+Sidecarless+Service+Mesh+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Simplifying Cloud-Native Security: eBPF-Powered Encryption in Sidecarless Service Mesh - Muyang Tian, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Muyang Tian, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcvl/project-lightning-talk-simplifying-cloud-native-security-ebpf-powered-encryption-in-sidecarless-service-mesh-muyang-tian-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Simplifying+Cloud-Native+Security%3A+eBPF-Powered+Encryption+in+Sidecarless+Service+Mesh+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Simplifying Cloud-Native Security: eBPF-Powered Encryption in Sidecarless Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvl/project-lightning-talk-simplifying-cloud-native-security-ebpf-powered-encryption-in-sidecarless-service-mesh-muyang-tian-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Simplifying+Cloud-Native+Security%3A+eBPF-Powered+Encryption+in+Sidecarless+Service+Mesh+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=D7vwFFeEn00
- YouTube title: Project Lightning Talk: Simplifying Cloud-Native Security: eBPF-Powered Encryption in... Muyang Tian
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-simplifying-cloud-native-security-ebpf-powered/D7vwFFeEn00.txt
- Transcript chars: 3615
- Keywords: mesh, traffic, encryption, packet, kernel, program, socket, ensure, encrypt, performance, information, security, native, source, scenario, overhead, governance, upload

### Resumo baseado na transcript

I'm Tamang from Hi Technologies and today I'm going to talk about the simplif cloud native security ebl powered encryption in static colorless mesh. The other is our um thinkings and implementations of um traffic encryption in cognitive scenario. At first the user set IPSAC preset keys in the Kubernetes as object secrets. Then the K mesh demon will generate IPSC ingress and ingress rules using the encryion information in the secret and note information in the API server. Also the kimsh demon will update the pure nodes information to a BFF try map and this map belongs to a TCBF program. So the final port will receive this packet and also our further work is to enable socket level encryption and the key design is socket migration and multi key management and in socket migration key mesh uh it will on the socket during TS handshake

### Excerpt da transcript

Hello everyone. I'm Tamang from Hi Technologies and today I'm going to talk about the simplif cloud native security ebl powered encryption in static colorless mesh. My topic has two parts. One for a brief introduction to our open source project key mesh. The other is our um thinkings and implementations of um traffic encryption in cognitive scenario. Let's start from first class. So um what is K mesh? So K mesh is a site colors EBPLF based and high performance with low overhead service mesh data plan. Here K is for kernel implying that we try to offload uh the traffic governance to kernel and the kimsh has been a project of CNCF landscape and also my colleagues shared about our projects during last year's kcom China. So let's see two modes of kes mesh and the first one is kernel mode. Here we um upload layer four and a simple layer 7 traffic governance to kernel and we build a transparent site color service mesh without passing through prox layer on data pass. So um this is to improve performance is low overhead and to ensure the service um awareness when ksh restarts or upgrades.

The other mode is D engine mode and here we upload layer four traffic to kernel uh but we process layer 7 traffic uh the traffic with point and this is to improve deployment flexibility and to ensure a transition smooth. Now comes the main topic. How to encrypt the traffic in cloud native scenario. The post manager by K mesh sends package to a specific NIC and the N will encrypt the package and send to the pier. The pers will uh uh will send to the service apps and this is link level encryption. K mesh integrates IPSAC as it encryption tool between nodes. Each node has a key mesh demon. At first the user set IPSAC preset keys in the Kubernetes as object secrets. Then the K mesh demon will generate IPSC ingress and ingress rules using the encryion information in the secret and note information in the API server. Also the kimsh demon will update the pure nodes information to a BFF try map and this map belongs to a TCBF program. So what's the purpose of this TC program? Now the port one tries to send packets to port two.

They are in different nodes. The TC program hook at Vither will be called during the packet processing. It will judge whether the remote port two is managed by K mesh. If so, it will mark the packet. In the next step, the market will match the rules in IPSAC. So the IBC will encrypt the packet and send it to the uh to the pier and the piercing will encrypt the pac
