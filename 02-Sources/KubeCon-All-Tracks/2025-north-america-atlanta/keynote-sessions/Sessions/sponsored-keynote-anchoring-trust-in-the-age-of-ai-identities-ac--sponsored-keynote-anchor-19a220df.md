---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Keynote Sessions"
themes: ["AI ML", "Security"]
speakers: ["Yuan Tang", "Senior Principal Software Engineer", "Red Hat", "Anjali Telang", "Senior Principal Product Manager for OpenShift Security and Identity", "Red Ha..."]
sched_url: https://kccncna2025.sched.com/event/27dCb/sponsored-keynote-anchoring-trust-in-the-age-of-ai-identities-across-humans-machines-and-models-yuan-tang-senior-principal-software-engineer-red-hat-anjali-telang-senior-principal-product-manager-for-openshift-security-and-identity-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Anchoring+Trust+in+the+Age+of+AI%3A+Identities+Across+Humans%2C+Machines%2C+and+Models+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Sponsored Keynote: Anchoring Trust in the Age of AI: Identities Across Humans, Machines, and Models - Yuan Tang, Senior Principal Software Engineer, Red Hat & Anjali Telang, Senior Principal Product Manager for OpenShift Security and Identity, Red Ha...

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Atlanta
- Speakers: Yuan Tang, Senior Principal Software Engineer, Red Hat, Anjali Telang, Senior Principal Product Manager for OpenShift Security and Identity, Red Ha...
- Schedule: https://kccncna2025.sched.com/event/27dCb/sponsored-keynote-anchoring-trust-in-the-age-of-ai-identities-across-humans-machines-and-models-yuan-tang-senior-principal-software-engineer-red-hat-anjali-telang-senior-principal-product-manager-for-openshift-security-and-identity-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Anchoring+Trust+in+the+Age+of+AI%3A+Identities+Across+Humans%2C+Machines%2C+and+Models+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Anchoring Trust in the Age of AI: Identities Across Humans, Machines, and Models.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27dCb/sponsored-keynote-anchoring-trust-in-the-age-of-ai-identities-across-humans-machines-and-models-yuan-tang-senior-principal-software-engineer-red-hat-anjali-telang-senior-principal-product-manager-for-openshift-security-and-identity-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Anchoring+Trust+in+the+Age+of+AI%3A+Identities+Across+Humans%2C+Machines%2C+and+Models+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qHrQVpy9HCg
- YouTube title: Sponsored Keynote: Anchoring Trust in the Age of AI: Identities Across... Y. Tang & A. Telang (ASL)
- Match score: 0.922
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sponsored-keynote-anchoring-trust-in-the-age-of-ai-identities-across-h/qHrQVpy9HCg.txt
- Transcript chars: 3229
- Keywords: identities, secure, identity, workloads, ai, across, humans, machines, models, connect, needed, keycloak, provides, cloudnative, ecosystem, spiffy, excited, revolution

### Resumo baseado na transcript

In the later stages of cloud and early stages of cloud native, we added capabilities to delegate authorization across services. First with OOTH, then with open ID connect, we layered identity on top so that web apps, APIs, and microservices could all trust who was calling. KSER is a standardized, scalable, and distributed model inference platform on Kubernetes for both generative and predictive AI. Queserve provides us a Kubernetes native way of deploying and managing AI models but wrapped in the same identity and authentication fabric that already secures our workloads through technologies like OIDC keycloak and OOTH. Please join us and contribute to security projects in the cloudnative community >> and come and explore Queser for how it provides a secure foundation for scalable AI workloads.

### Excerpt da transcript

Thank you so much. Good morning and hello Atlanta. >> Hello everyone. Super excited to be here today. >> So every revolution in computing has been defined by trust. When the internet exploded, we built firewalls. Then when the cloud arose, we used cryptographic keys and AM roles. In the later stages of cloud and early stages of cloud native, we added capabilities to delegate authorization across services. First with OOTH, then with open ID connect, we layered identity on top so that web apps, APIs, and microservices could all trust who was calling. But just providing specification was not enough. We needed implementation. The CNCF keycloak project provides implementation of oath and open ID connect to all cloudnative developers and users. Now each time we added new capabilities, each time we added new things to secure and new ways to secure them. But humans were not the only ones that needed identities. Microservices were exploding. Machines needed identities, too. This is when the CNCF ecosystem came together and we saw the rise of Spiffy and Spire, a universal standard and runtime system for cryptographic workload identities.

For the first time, machine identities had an equal standing with human identities. >> And as AI becomes a we need to employ the same level of identity for AI workloads. Think about it. An AI agent may call an external API, chain multiple services, or spin up shortlived workloads. Without strong and runtime attested identity, it's just impossible to secure or audit. This is where KSER steps in to help with the model inference, which is a foundation for agentic AI. KSER is a standardized, scalable, and distributed model inference platform on Kubernetes for both generative and predictive AI. And today we're super excited to share with all of you that Queser has just joined CNF as an incubating project. [applause] Thank you. It's so inspiring to see so many of you contributing and adopting Keserve and we really look forward to continuing building on that momentum and deepening our collaboration within the cloudnative ecosystem. Queserve provides us a Kubernetes native way of deploying and managing AI models but wrapped in the same identity and authentication fabric that already secures our workloads through technologies like OIDC keycloak and OOTH.

So as we look at this next revolution, the age of agentic AI, we don't have to rebuild trust, the CNCF ecosystem has already given us the building blocks for it. By weaving together Kerf,
