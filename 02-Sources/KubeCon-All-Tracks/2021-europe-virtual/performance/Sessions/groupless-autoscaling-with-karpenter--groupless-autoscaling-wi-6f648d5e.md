---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Performance"
themes: ["SRE Reliability"]
speakers: ["Ellis Tarn", "Prateek Gogia", "Amazon"]
sched_url: https://kccnceu2021.sched.com/event/iE30/groupless-autoscaling-with-karpenter-ellis-tarn-prateek-gogia-amazon
youtube_search_url: https://www.youtube.com/results?search_query=Groupless+Autoscaling+with+Karpenter+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Groupless Autoscaling with Karpenter - Ellis Tarn & Prateek Gogia, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Ellis Tarn, Prateek Gogia, Amazon
- Schedule: https://kccnceu2021.sched.com/event/iE30/groupless-autoscaling-with-karpenter-ellis-tarn-prateek-gogia-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=Groupless+Autoscaling+with+Karpenter+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Groupless Autoscaling with Karpenter.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE30/groupless-autoscaling-with-karpenter-ellis-tarn-prateek-gogia-amazon
- YouTube search: https://www.youtube.com/results?search_query=Groupless+Autoscaling+with+Karpenter+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=43g8uPohTgc
- YouTube title: Groupless Autoscaling with Karpenter - Ellis Tarn & Prateek Gogia, Amazon
- Match score: 0.772
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/groupless-autoscaling-with-karpenter/43g8uPohTgc.txt
- Transcript chars: 33027
- Keywords: cluster, instance, carpenter, capacity, running, seconds, actually, groups, scheduling, created, instances, pending, scheduler, another, scaling, provider, create, scaler

### Resumo baseado na transcript

hi everyone welcome to our session on group less auto skilling with carpenter my name is priti gogia and i am here with alistan we both work in the ek scalability team at aws we have been working on the carpenter project for last few months and today we will be talking about the current auto scaling landscape in kubernetes how carpenter works and a quick short demo there are multiple ways a part can be created in a cluster users can use a clr tool like cube ctl or and the image is being pulled in the background so they both are in the running states on an arm architecture so yeah this is all i had for the demo thanks for joining our session

### Excerpt da transcript

hi everyone welcome to our session on group less auto skilling with carpenter my name is priti gogia and i am here with alistan we both work in the ek scalability team at aws we have been working on the carpenter project for last few months and today we will be talking about the current auto scaling landscape in kubernetes how carpenter works and a quick short demo there are multiple ways a part can be created in a cluster users can use a clr tool like cube ctl or there could be a cron job running or there could be an auto scaler tool such as hpa cada k native which could add these part into the cluster once these spots are added they need resources to be able to run these resources can either be added by a manual effort or by an auto scaler capacity planning is hard and manual scaling can be slow error prone and cause significant delays as compared to an auto scaler auto skiller has benefits over manual and today cluster auto scaler has become the de facto for auto scaling in kubernetes so what are the some of the benefits of cluster autoscaler as part scale up load increases in the cluster cluster autoscaler can request more capacity from the underlying provider and when the load reduces the cluster auto scaler can also request to terminate these instances from the provider which in turn helps user reduce their infrastructure costs and remove the burden of capacity planning there are other advantages such as closer autoscaler is vendor neutral so has support for all the major crowd providers the approach is battle tested and widely adopted and it works great for cluster sizes about 1000 nodes so let's take a look at how closer autoscaler works cluster autoscaler works around this concept of node groups which is an auto scaling group or an asg in case of an in case of aws it looks for pending parts sets the desired count of instances based on the number of pending parts on a node group once the underlying provider provisions the capacity based on the desired count cube scheduler places these parts onto these new nodes being created node group here plays critical role by maintaining the desired number of nodes which are requested by the auto scaler so let's try to understand what node group is node group is a logical grouping of nodes which can be auto scaled and managed together cluster admins can create these multiple node groups specifying instance type options and some other configurations and also set a minimum and a max node count node groups are not
