from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    """Only can access non-destructive methods"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS

class AdminOnly(ReadOnly):
    """Only Admin can access"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)
    
            

    def has_object_permission(self, request, view, obj=None):
        if(request.user.is_superuser):
            return request.user.is_superuser
        else:
            return super(AdminOnly,self).has_object_permission(request, view,obj)


