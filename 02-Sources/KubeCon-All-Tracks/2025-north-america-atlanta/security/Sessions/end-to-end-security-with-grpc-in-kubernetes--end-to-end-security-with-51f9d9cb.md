---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Shiva", "Abhishek Agrawal", "Google"]
sched_url: https://kccncna2025.sched.com/event/27FVP/end-to-end-security-with-grpc-in-kubernetes-shiva-abhishek-agrawal-google
youtube_search_url: https://www.youtube.com/results?search_query=End-to-End+Security+With+gRPC+in+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# End-to-End Security With gRPC in Kubernetes - Shiva & Abhishek Agrawal, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Shiva, Abhishek Agrawal, Google
- Schedule: https://kccncna2025.sched.com/event/27FVP/end-to-end-security-with-grpc-in-kubernetes-shiva-abhishek-agrawal-google
- Busca YouTube: https://www.youtube.com/results?search_query=End-to-End+Security+With+gRPC+in+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre End-to-End Security With gRPC in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVP/end-to-end-security-with-grpc-in-kubernetes-shiva-abhishek-agrawal-google
- YouTube search: https://www.youtube.com/results?search_query=End-to-End+Security+With+gRPC+in+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fhjiLyntYBg
- YouTube title: End-to-End Security With gRPC in Kubernetes - Shiva & Abhishek Agrawal, Google
- Match score: 0.821
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/end-to-end-security-with-grpc-in-kubernetes/fhjiLyntYBg.txt
- Transcript chars: 19725
- Keywords: mesh, security, sidecar, control, server, resource, management, certificate, client, application, traffic, proxyless, configuration, identity, resources, cluster, envoy, provides

### Resumo baseado na transcript

Over the next session, we are going to walk you through the entire security journey starting from the basics of TLS, moving through the operational challenges in Kubernetes and finally looking at advanced solutions like service mesh and proxyless GPC. The content and views presented during this session are our personal views and do not represent any organizations we are associated with or employed at let's start to the to set the stage. So does this configuration help solve all our problem and we can move on with our lives to more important things like collecting swags? Search manager talks to the issuer, gets the certificate and saves it as a standard Kubernetes secret. So the finally the full Kubernetes uh native flow is deploy manager create your issuer request the certificate and mount the secret and also you need to update your app code to read from that file path. The when the certificate is about to expire, search manager renews it, updates the secret and uh it also Kubernetes also updates the file inside the pod.

### Excerpt da transcript

Hi everyone and welcome. Uh it's great to be here at CubeCon Atlanta. I am Abshik and I'm here with my colleague Shiva. We are software devs at Google working on the GPC team. Over the next session, we are going to walk you through the entire security journey starting from the basics of TLS, moving through the operational challenges in Kubernetes and finally looking at advanced solutions like service mesh and proxyless GPC. Cool. Um before proceeding just a short disclaimer. The content and views presented during this session are our personal views and do not represent any organizations we are associated with or employed at let's start to the to set the stage. Uh let's look at the two technologies during this conversation. microservices and GC. We have moved away from large monoliths to building systems um as suites of small independent services. And for these services to talk to each other, gRPC has become the industry standard. Why? Because it's a high performance and built specifically for this environment.

It runs on HTTP2 for efficiency. It uses Probab for lightweight serialization and supports birectional streaming out of the box. It's the perfect glue for a microservices architecture. But this architecture introduces new risks especially in Kubernetes. First, it's dynamic. Pots come and go. IPs change constantly. You can't rely on static firewall rules. Second, it's usually a flat network. By default, any pod can talk to any other pod. If one service is compromised, the attacker has a clear path to everything else. This is why we need end to-end security. We need to ensure that we trust exactly who we are talking to regardless of the network. Cool. The baseline for this trust is TLS. It gives us three things. Authentication, which is verifying the server, encryption, so no one can snoop on the wire. And integrity, so no one can tamper with the data. Most of you know this, but in gc, these three are absolute non-negotiables. All right. Uh in code, it looks something like this. On the server which is on the left, we load the certificate chain and private key.

This proves the server's identity. On the client, which is on the right, we load the CA certificate. This tells the client which authorities to trust. So does this configuration help solve all our problem and we can move on with our lives to more important things like collecting swags? Sadly no. While this is simple enough for one service, we need to go further. MTLS the standard TLS only prote
