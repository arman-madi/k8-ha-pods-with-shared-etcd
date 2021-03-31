# k8-ha-pods-with-shared-etcd
Demonstrate high-availability kubernetes pods working collaboratively in an active-active style, thanks to etcd features.

Running multiple instance of a simple script which is called distributed-counter, to see how to do a synchronization between pods by using etcd as shared storage between them.      
<code>
kubectl apply -f ./deployment.yaml
</code>