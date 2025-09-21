import asyncio
from typing import Dict, Any, Optional, List
from InstaLiveCLI import InstaLiveCLI


class InstagramService:
    _instances: Dict[str, 'InstagramService'] = {}

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.ig_client: Optional[InstaLiveCLI] = None
        self.is_authenticated = False
        self.stream_data = {}

    @classmethod
    def get_instance(cls, username: str) -> Optional['InstagramService']:
        return cls._instances.get(username)

    async def login(self) -> bool:
        try:
            loop = asyncio.get_event_loop()
            self.ig_client = InstaLiveCLI(username=self.username, password=self.password)

            # Run Instagram login in thread pool to avoid blocking
            login_result = await loop.run_in_executor(None, self.ig_client.login)

            if login_result:
                self.is_authenticated = True
                self._instances[self.username] = self

                # Create initial broadcast
                await self.create_broadcast()
                return True

            return False

        except Exception as e:
            print(f"Login error: {str(e)}")
            return False

    async def create_broadcast(self) -> Dict[str, Any]:
        if not self.is_authenticated or not self.ig_client:
            return {"success": False, "message": "Not authenticated"}

        try:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, self.ig_client.create_broadcast)

            self.stream_data = {
                "status": "ready",
                "stream_url": self.ig_client.settings.get("data_stream", {}).get("stream_url"),
                "stream_key": self.ig_client.settings.get("data_stream", {}).get("stream_key"),
                "broadcast_id": self.ig_client.settings.get("data_stream", {}).get("broadcast_id")
            }

            return {
                "success": True,
                "message": "Broadcast created successfully",
                "data": self.stream_data
            }

        except Exception as e:
            return {"success": False, "message": f"Failed to create broadcast: {str(e)}"}

    async def start_broadcast(self) -> Dict[str, Any]:
        if not self.is_authenticated or not self.ig_client:
            return {"success": False, "message": "Not authenticated"}

        try:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, self.ig_client.start_broadcast)

            if result:
                self.stream_data["status"] = "running"
                return {
                    "success": True,
                    "message": "Broadcast started successfully",
                    "data": self.stream_data
                }
            else:
                return {"success": False, "message": "Failed to start broadcast"}

        except Exception as e:
            return {"success": False, "message": f"Failed to start broadcast: {str(e)}"}

    async def stop_broadcast(self) -> Dict[str, Any]:
        if not self.is_authenticated or not self.ig_client:
            return {"success": False, "message": "Not authenticated"}

        try:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, self.ig_client.end_broadcast)

            if result:
                self.stream_data["status"] = "stopped"
                return {
                    "success": True,
                    "message": "Broadcast stopped successfully",
                    "data": self.stream_data
                }
            else:
                return {"success": False, "message": "Failed to stop broadcast"}

        except Exception as e:
            return {"success": False, "message": f"Failed to stop broadcast: {str(e)}"}

    async def get_stream_info(self) -> Dict[str, Any]:
        if not self.is_authenticated or not self.ig_client:
            return {"status": "not_authenticated"}

        try:
            loop = asyncio.get_event_loop()
            status = await loop.run_in_executor(None, self.ig_client.get_broadcast_status)

            self.stream_data["status"] = status
            return self.stream_data

        except Exception as e:
            return {"status": "error", "message": str(e)}

    async def get_viewers(self) -> List[str]:
        if not self.is_authenticated or not self.ig_client:
            return []

        try:
            loop = asyncio.get_event_loop()
            viewers, viewer_ids = await loop.run_in_executor(None, self.ig_client.get_viewer_list)
            return viewers or []

        except Exception as e:
            print(f"Error getting viewers: {str(e)}")
            return []